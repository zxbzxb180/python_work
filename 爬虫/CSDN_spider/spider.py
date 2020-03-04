import re
import ast

import requests
from urllib import parse
import time
from selenium import webdriver
from scrapy import Selector
from datetime import datetime

from models import *


def get_nodes_json():
    left_menu_text = requests.get('https://bbs.csdn.net/dynamic_js/left_menu.js?csdn').text
    nodes_str_match = re.search('forumNodes: (.*])', left_menu_text)
    if nodes_str_match:
        nodes_str = nodes_str_match.group(1).replace('null', 'None')
        nodes_list = ast.literal_eval(nodes_str)  # 执行字符串，这里可以将字符串转换成list（本字符串是list的结构）
        return nodes_list
    return []


def process_nodes_list(url_list, nodes_list):
    # 将js格式的list提取出url到url_list
    for item in nodes_list:
        if 'url' in item:
            if item['url']:
                url_list.append(item['url'])
            if 'children' in item:
                process_nodes_list(url_list, item['children'])


def get_level1_list(nodes_list):
    level1_list = []
    for item in nodes_list:
        if 'url' in item and item['url']:
            if item['url']:
                level1_list.append(item['url'])
    return level1_list


def get_last_url_list(url_list):
    # 获取非顶层板块的url
    last_url_list = []
    nodes_list = get_nodes_json()
    process_nodes_list(url_list, nodes_list)
    level1_list = get_level1_list(nodes_list)

    for url in url_list:
        if url not in level1_list:
            last_url_list.append(parse.urljoin(domain, url))
            last_url_list.append(parse.urljoin(domain, url+'/recommend'))
            last_url_list.append(parse.urljoin(domain, url+'/closed'))
    return last_url_list


def get_cookie():
    browser = webdriver.Chrome()
    browser.get('https://bbs.csdn.net/forums/ios')
    time.sleep(5)
    all_cookie = browser.get_cookies()
    cookie_dict = {}
    for item in all_cookie:
        cookie_dict[item['name']] = item['value']
    print(cookie_dict)
    return cookie_dict


def parse_topic(url):
    # 获取帖子详情及回复
    topic_id = url.split('/')[-1]
    if "?" in topic_id:
        topic_id = topic_id.split("?")[0]
    res_text = requests.get(url, cookies=cookie_dict, headers=headers).text
    sel = Selector(text=res_text)
    all_divs = sel.xpath("//div[starts-with(@id, 'post-')]")
    topic_item = all_divs[0]
    content = topic_item.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]
    praised = topic_item.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
    jtl_str = topic_item.xpath(".//div[@class='close_topic']/text()").extract()
    jtl_str = "".join(jtl_str).strip()
    jtl = 0  # 默认
    jtl_match = re.search('\d+(\.\d+)?', jtl_str)
    if jtl_match:
        jtl = jtl_match.group()

    existed_topics = Topic.select().where(Topic.id == topic_id)
    if existed_topics:
        topic = existed_topics[0]
        topic.content = content
        topic.praised_nums = praised
        topic.jtl = jtl
        topic.save()

    for answer_item in all_divs[1:]:
        author_info = answer_item.xpath(".//div[@class='nick_name']/a/@href").extract()[0]
        author_id = author_info.split('/')[-1]
        create_time_str = answer_item.xpath(".//label[@class='date_time']/text()").extract()[0]
        create_time = datetime.strptime(create_time_str, '%Y-%m-%d %H:%M:%S')
        praised = answer_item.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
        content = answer_item.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]

        answer = Answer()
        answer.topic_id = int(topic_id)
        answer.author = author_id
        answer.create_time = create_time
        answer.praised_nums = int(praised)
        answer.content = content

        answer.save()

    next_page = sel.xpath("//a[@class='pageliststy next_page']/@href").extract()
    if next_page:
        next_url = parse.urljoin(domain, next_page[0])
        parse_topic(next_url)


def parse_author_blog(url):
    # 获取用户博客页面数据
    author_id = url.split("/")[-1]
    res_text = requests.get(url, headers=headers, cookies=cookie_dict).text
    sel = Selector(text=res_text)
    all_list = sel.xpath("//div[@class='data-info d-flex item-tiling']/dl/@title").extract()
    if not all_list:
        return
    original_nums = int(all_list[0])
    follower_nums = int(all_list[1])
    praised_nums = int(all_list[2])
    answer_nums = int(all_list[3])
    click_nums = int(all_list[4])
    rate_str = sel.xpath("//div[@class='grade-box clearfix']/dl/@title").extract()[0]
    if rate_str == '暂无排名':
        rate_str = -1
    rate = int(rate_str)
    name_str = sel.xpath("//div[@class='profile-intro d-flex']//span[@class='name csdn-tracking-statistics tracking-click ']/a/text()").extract()
    name = "".join(name_str).strip()

    existed_author = Author.select().where(Author.id == author_id)
    if existed_author:
        author = existed_author[0]
        author.original_nums = original_nums
        author.follower_nums = follower_nums
        author.praised_nums = praised_nums
        author.answer_nums = answer_nums
        author.click_nums = click_nums
        author.rate = rate
        author.name = name
        author.save()


def parse_author(url):
    # 获取用户详情页面数据
    author = Author()
    author_id = url.split('/')[-1]
    res_text = requests.get(url, headers=headers, cookies=cookie_dict).text
    sel = Selector(text=res_text)
    author_info = sel.xpath("//div[@class='lt_main clearfix']")
    desc_str = author_info.xpath("./div[@class='description clearfix']/p[@class='description_detail']/text()").extract()
    if desc_str:
        desc = "".join(desc_str).strip()
        author.desc = desc
    following_nums_str = sel.xpath("//div[@class='me_fans clearfix']/div[@class='att']//span/text()").extract()[0]
    following_nums = int(following_nums_str)
    author.following_nums = following_nums
    author.id = author_id

    existed_author = Author.select().where(Author.id == author_id)
    if existed_author:
        author.save()
    else:
        author.save(force_insert=True)

    blog_url_list = url.split('.')
    blog_url_list[0] = 'https://blog'
    blog_url = '.'.join(blog_url_list)

    parse_author_blog(blog_url)


def parse_list(url):
    # 获取帖子列表页
    res_text = requests.get(url, cookies=cookie_dict, headers=headers).text
    sel = Selector(text=res_text)
    all_trs = sel.xpath("//table[@class='forums_tab_table']/tbody/tr")
    for tr in all_trs:
        status = tr.xpath(".//td[1]/span/text()").extract()[0]
        score = tr.xpath(".//td[2]/em/text()").extract()[0]
        topic_url = parse.urljoin(domain, tr.xpath(".//td[3]/a[contains(@class, 'forums_title')]/@href").extract()[0])
        topic_id = int(topic_url.split('/')[-1])
        topic_title = tr.xpath(".//td[3]/a[contains(@class, 'forums_title')]/text()").extract()[0]
        author_url = parse.urljoin(domain, tr.xpath(".//td[4]/a/@href").extract()[0])
        author_id = author_url.split('/')[-1]  # 是用户id  不是用户名，id唯一
        creat_time_str = tr.xpath(".//td[4]/em/text()").extract()[0]
        creat_time = datetime.strptime(creat_time_str, '%Y-%m-%d %H:%M')
        answer_info = tr.xpath(".//td[5]/span/text()").extract()[0]
        answer_nums = answer_info.split('/')[0]
        click_nums = answer_info.split('/')[1]
        last_time_str = tr.xpath(".//td[6]/em/text()").extract()[0]
        last_time = datetime.strptime(last_time_str, '%Y-%m-%d %H:%M')

        topic = Topic()
        topic.id = topic_id
        topic.title = topic_title
        topic.author = author_id
        topic.create_time = creat_time
        topic.answer_nums = int(answer_nums)
        topic.click_nums = int(click_nums)
        topic.last_answer_time = last_time
        topic.score = int(score)
        topic.status = status

        existed_topics = Topic.select().where(Topic.id == topic.id)
        if existed_topics:
            topic.save()
        else:
            topic.save(force_insert=True)

        parse_topic(topic_url)
        parse_author(author_url)

    next_page = sel.xpath("//a[@class='pageliststy next_page']/@href").extract()
    if next_page:
        next_url = parse.urljoin(domain, next_page[0])
        parse_list(next_url)


if __name__ == '__main__':
    domain = 'https://bbs.csdn.net/'
    # 获取cookie
    cookie_dict = get_cookie()
    # 设置headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    urls = []
    last_url_list = get_last_url_list(urls)
    # last_url_list = ['https://bbs.csdn.net/forums/ios']
    for last_url in last_url_list:
        parse_list(last_url)