import json

import requests
from scrapy import Selector


def parse_good(good_id):
    good_url = 'https://item.jd.com/{}.html'.format(good_id)
    html = requests.get(good_url).text

    sel = Selector(text=html)
    name = sel.xpath("//div[@class='sku-name']/text()").extract()[0].strip()
    price_url = 'https://p.3.cn/prices/mgets?type=1&pdbp=0&skuIds=J_{}&source=item-pc'.format(good_id)
    price_json = requests.get(price_url).text.strip()
    price_list = json.loads(price_json)
    if price_list:
        price = float(price_list[0]['p'])
    pass


if __name__ == '__main__':
    parse_good(100004286349)