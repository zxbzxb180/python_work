# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from eastmoney.items import EastmoneyItem
from scrapy import Request


class AsiaSpiderSpider(scrapy.Spider):
    name = 'asia_spider'
    allowed_domains = ['quote.eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/center/gridlist.html#global_asia']

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = self.start_urls
            yield Request(url='http://quote.eastmoney.com/center/gridlist.html#global_asia',callback=self.parse,meta={'page':page},dont_filter=True)

    def parse(self, response):
        asia_list = response.xpath("//div[@class='row']//table[@id='table_wrapper-table']//tbody/tr")
        for asia_item in asia_list:
            item = EastmoneyItem()
            item['number'] = asia_item.xpath(".//td[1]/text()").extract_first()
            item['name'] = asia_item.xpath(".//td[2]/a/text()").extract_first()
            item['latest_price'] = asia_item.xpath(".//td[3]//text()").extract_first()
            item['amount_of_rise_and_fall'] = asia_item.xpath(".//td[4]//text()").extract_first()
            item['rate_of_rise_and_fall'] = asia_item.xpath(".//td[5]//text()").extract_first()
            item['today_opening_price'] = asia_item.xpath(".//td[6]//text()").extract_first()
            item['maximum_price'] = asia_item.xpath(".//td[7]//text()").extract_first()
            item['minimum_price'] = asia_item.xpath(".//td[8]//text()").extract_first()
            item['yesterday_closing_price'] = asia_item.xpath(".//td[9]/text()").extract_first()
            item['amplitude'] = asia_item.xpath(".//td[10]/text()").extract_first()
            item['update_time'] = asia_item.xpath(".//td[11]/text()").extract_first()
            yield item


