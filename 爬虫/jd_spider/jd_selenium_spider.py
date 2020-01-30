import json
import time
import re
from datetime import datetime

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from scrapy import Selector

from 爬虫.jd_spider.models import *
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# 设置chrome的无界面模式
chrome_options.add_argument("--headless")

# 设置不加载图片
chrome_options.add_argument("blink-settings=imagesEnabled=false")

# 谷歌文档提示加上这个属性用来规避bug
chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(chrome_options=chrome_options)


def str_to_int(nums_str):
    """
    将评价的字符串转为整型
    :param nums_str: 数字字符串，可能出现"万"
    :return: 整型数字，默认为0
    """
    nums = 0
    re_search = re.search("(\d+)", nums_str)
    if re_search:
        nums = int(re_search.group(1))
        if "万" in nums_str:
            nums *= 10000
    return nums


def parse_good(good_id):
    browser.get('https://item.jd.com/{}.html'.format(good_id))

    sel = Selector(text=browser.page_source)

    # 提取商品基本信息
    good = Good()
    good.id = good_id
    name = "".join(sel.xpath("//div[@class='sku-name']/text()").extract()).strip()
    price = float("".join(sel.xpath("//span[@class='price J-p-{}']/text()".format(good_id)).extract()).strip())
    detail = "".join(sel.xpath("//div[@id='detail']//div[@class='tab-con']").extract()).strip()
    good_images = sel.xpath("//div[@id='spec-list']//img/@src").extract()
    supplier_info = "".join(sel.xpath("//div[@id='summary-service']").extract()[0])

    good.name = name
    good.price = price
    good.image_list = json.dumps(good_images)
    good.content = detail

    # 模拟点击规格包装

    ggbz_element = browser.find_element_by_xpath("//div[@class='tab-main large']//li[contains(text(), '规格与包装')]")
    ggbz_element.click()
    time.sleep(5)

    sel = Selector(text=browser.page_source)
    ggbz = "".join(sel.xpath("//div[@id='detail']/div[@class='tab-con']").extract())
    good.ggbz = ggbz

    # 模拟点击商品评价
    evaluate_element = browser.find_element_by_xpath("//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")
    evaluate_element.click()
    time.sleep(5)

    sel = Selector(text=browser.page_source)
    tag_list = sel.xpath("//div[@class='tag-list tag-available']/span/text()").extract()
    good_rate = int(sel.xpath("//div[@class='percent-con']/text()").extract()[0])
    good.good_rate = good_rate

    summary_as = sel.xpath("//ul[@class='filter-list']/li")
    for summary_a in summary_as[:7]:
        name = summary_a.xpath("./a/text()").extract()[0]
        nums_str = summary_a.xpath("./@data-num").extract()[0]
        nums = str_to_int(nums_str)

        if name == '晒图':
            good.has_image_evaluate_nums = nums
        elif name == '视频晒单':
            good.has_video_evaluate_nums = nums
        elif name == '追评':
            good.has_add_evaluate_nums = nums
        elif name == '好评':
            good.well_evaluate_nums = nums
        elif name == '中评':
            good.middle_evaluate_nums = nums
        elif name == '差评':
            good.bad_evaluate_nums = nums
        elif name == '全部评价':
            good.evaluate_nums = nums

    # 保存商品信息
    existed_good = Good.select().where(Good.id == good_id)
    if existed_good:
        good.save()
    else:
        good.save(force_insert=True)

    for tag in tag_list:
        re_match = re.match("(.*)\((\d+)\)", tag)
        if re_match:
            tag_name = re_match.group(1)
            num = int(re_match.group(2))

            # 去重
            existed_summary = GoodEvaluateSummary.select().where(GoodEvaluateSummary.good == good, GoodEvaluateSummary.tag == tag_name)
            if existed_summary:
                summary = existed_good[0]
            else:
                summary = GoodEvaluateSummary(good=good)
            summary.tag = tag_name
            summary.num = num
            summary.save()

    # 获取商品评价
    has_next_page = True
    while has_next_page:
        all_evaluates = sel.xpath("//div[@class='comment-item']")
        for evaluate in all_evaluates:
            evaluate_id = evaluate.xpath("./@data-guid").extract()[0]
            good_evaluate = GoodEvaluate(good=good, id=evaluate_id)

            user_head_url = evaluate.xpath(".//div[@class='user-info']/img/@src").extract()[0]
            good_evaluate.user_head_url = user_head_url

            user_name = "".join(evaluate.xpath(".//div[@class='user-info']/text()").extract()).strip()
            good_evaluate.user_name = user_name

            star_str = evaluate.xpath("./div[2]/div[1]/@class").extract()[0]
            star = int(star_str[-1])
            good_evaluate.star = star

            evaluate_content = "".join(evaluate.xpath("./div[2]//p[@class='comment-con']/text()").extract()).strip()
            good_evaluate.content = evaluate_content

            image_list = evaluate.xpath("./div[2]//div[@class='pic-list J-pic-list']/a/img/@src").extract()
            good_evaluate.image_list = json.dumps(image_list)

            video_list = evaluate.xpath("./div[2]//div[@class='J-video-view-wrap clearfix']//video/@src").extract()
            good_evaluate.video_list = json.dumps(video_list)

            praised_nums = evaluate.xpath("./div[2]//div[@class='comment-op']/a[2]/text()").extract()[0]
            good_evaluate.praised_nums = praised_nums

            comment_nums = evaluate.xpath("./div[2]//div[@class='comment-op']/a[3]/text()").extract()[0]
            good_evaluate.comment_nums = comment_nums

            info = evaluate.xpath("./div[2]//div[@class='order-info']/span/text()").extract()
            good_info = info[:-1]
            good_evaluate.good_info = json.dumps(good_info)

            evaluate_time = info[-1]
            good_evaluate.evaluate_time = datetime.strptime(evaluate_time, '%Y-%m-%d %H:%M')

            # 保存
            existed_evaluate = GoodEvaluate.select().where(GoodEvaluate.id == evaluate_id)
            if existed_evaluate:
                good_evaluate.save()
            else:
                good_evaluate.save(force_insert=True)
        try:
            next_page_element = browser.find_element_by_xpath("//div[@id='comment']//a[@class='ui-pager-next']")
            # next_page_element.click()
            next_page_element.send_keys("\n")
            time.sleep(5)
            sel = Selector(text=browser.page_source)
        except NoSuchElementException as e:
            has_next_page = False

    pass


if __name__ == '__main__':
    parse_good(100004404920)