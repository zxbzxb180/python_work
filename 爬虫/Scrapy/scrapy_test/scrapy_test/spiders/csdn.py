# -*- coding: utf-8 -*-
from urllib import parse
from datetime import datetime
import re

import scrapy
from scrapy.http import Request

from scrapy_test.models import *
from scrapy_test.items import *


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://bbs.csdn.net/forums/ios']
    domain = 'https://bbs.csdn.net/'

    def parse(self, response):
        # 获取帖子列表页
        all_trs = response.xpath("//table[@class='forums_tab_table']/tbody/tr")
        for tr in all_trs:
            status = tr.xpath(".//td[1]/span/text()").extract()[0]
            score = tr.xpath(".//td[2]/em/text()").extract()[0]
            topic_url = parse.urljoin(self.domain,
                                      tr.xpath(".//td[3]/a[contains(@class, 'forums_title')]/@href").extract()[0])
            topic_id = int(topic_url.split('/')[-1])
            topic_title = tr.xpath(".//td[3]/a[contains(@class, 'forums_title')]/text()").extract()[0]
            author_url = parse.urljoin(self.domain, tr.xpath(".//td[4]/a/@href").extract()[0])
            author_id = author_url.split('/')[-1]  # 是用户id  不是用户名，id唯一
            creat_time_str = tr.xpath(".//td[4]/em/text()").extract()[0]
            creat_time = datetime.strptime(creat_time_str, '%Y-%m-%d %H:%M')
            answer_info = tr.xpath(".//td[5]/span/text()").extract()[0]
            answer_nums = answer_info.split('/')[0]
            click_nums = answer_info.split('/')[1]
            last_time_str = tr.xpath(".//td[6]/em/text()").extract()[0]
            last_time = datetime.strptime(last_time_str, '%Y-%m-%d %H:%M')

            topic = TopicItem_1()
            topic['id'] = topic_id
            topic['title'] = topic_title
            topic['author'] = author_id
            topic['create_time'] = creat_time
            topic['answer_nums'] = int(answer_nums)
            topic['click_nums'] = int(click_nums)
            topic['last_answer_time'] = last_time
            topic['score'] = int(score)
            topic['status'] = status

            yield topic

            yield Request(url=topic_url, callback=self.parse_topic)
            yield Request(url=author_url, callback=self.parse_author)

        next_page = response.xpath("//div[@class='page_nav']/a[@class='pageliststy next_page']/@href").extract()
        if next_page:
            next_url = parse.urljoin(self.domain, next_page[0])
            yield Request(url=next_url, callback=self.parse)

    def parse_topic(self, response):
        # 获取帖子详情及回复
        url = response.url
        topic_id = url.split('/')[-1]
        if "?" in topic_id:
            topic_id = topic_id.split("?")[0]
        all_divs = response.xpath("//div[starts-with(@id, 'post-')]")
        topic_item = all_divs[0]
        content = topic_item.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]
        praised = topic_item.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
        jtl_str = topic_item.xpath(".//div[@class='close_topic']/text()").extract()
        jtl_str = "".join(jtl_str).strip()
        jtl = 0  # 默认
        jtl_match = re.search('\d+(\.\d+)?', jtl_str)
        if jtl_match:
            jtl = jtl_match.group()

        topic = TopicItem_2()
        topic['id'] = topic_id
        topic['content'] = content
        topic['praised_nums'] = praised
        topic['jtl'] = jtl
        yield topic

        for answer_item in all_divs[1:]:
            author_info = answer_item.xpath(".//div[@class='nick_name']/a/@href").extract()[0]
            author_id = author_info.split('/')[-1]
            create_time_str = answer_item.xpath(".//label[@class='date_time']/text()").extract()[0]
            create_time = datetime.strptime(create_time_str, '%Y-%m-%d %H:%M:%S')
            praised = answer_item.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
            content = answer_item.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]

            answer = AnswerItem()
            answer['topic_id'] = int(topic_id)
            answer['author'] = author_id
            answer['create_time'] = create_time
            answer['praised_nums'] = int(praised)
            answer['content'] = content

            yield answer

        next_page = response.xpath("//div[@class='page_nav']/a[@class='pageliststy next_page']/@href").extract()
        if next_page:
            next_url = parse.urljoin(self.domain, next_page[0])
            yield Request(url=next_url, callback=self.parse_topic)

    def parse_author(self, response):
        # 获取用户详情页面数据
        author = AuthorItem()
        url = response.url
        author_id = url.split('/')[-1]

        author_info = response.xpath("//div[@class='lt_main clearfix']")
        desc_str = author_info.xpath(
            "./div[@class='description clearfix']/p[@class='description_detail']/text()").extract()
        if desc_str:
            desc = "".join(desc_str).strip()
            author['desc'] = desc
        following_nums_str = response.xpath("//div[@class='me_fans clearfix']/div[@class='att']//span/text()").extract()[0]
        following_nums = int(following_nums_str)
        author['following_nums'] = following_nums
        author['id'] = author_id

        yield author

        blog_url_list = url.split('.')
        blog_url_list[0] = 'https://blog'
        blog_url = '.'.join(blog_url_list)

        yield Request(url=blog_url, callback=self.parse_author_blog)

    def parse_author_blog(self, response):
        # 获取用户博客页面数据
        url = response.url
        author_id = url.split("/")[-1]

        all_list = response.xpath("//div[@class='data-info d-flex item-tiling']/dl/@title").extract()
        if not all_list:
            return
        original_nums = int(all_list[0])
        follower_nums = int(all_list[1])
        praised_nums = int(all_list[2])
        answer_nums = int(all_list[3])
        click_nums = int(all_list[4])
        rate_str = response.xpath("//div[@class='grade-box clearfix']/dl/@title").extract()[0]
        if rate_str == '暂无排名':
            rate_str = -1
        rate = int(rate_str)
        name_str = response.xpath(
            "//div[@class='profile-intro d-flex']//span[@class='name csdn-tracking-statistics tracking-click ']/a/text()").extract()
        name = "".join(name_str).strip()

        authorblog = AuthorBlogItem()
        authorblog['id'] = author_id
        authorblog['original_nums'] = original_nums
        authorblog['follower_nums'] = follower_nums
        authorblog['praised_nums'] = praised_nums
        authorblog['answer_nums'] = answer_nums
        authorblog['click_nums'] = click_nums
        authorblog['rate'] = rate
        authorblog['name'] = name

        yield authorblog