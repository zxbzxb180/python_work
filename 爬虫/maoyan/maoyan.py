import requests
import re
import time
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {
        'User-Agent':'(Macintosh;Intel Mac OS X 10_13_3)ApplewebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return '错误'

def main(offset):
    url = 'http://maoyan.com/board/4?iffset=&offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip()+item[6].strip()
        }


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)