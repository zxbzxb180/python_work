import requests
from fake_useragent import UserAgent

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

from scrapy import Selector


def zhihu_login(account, password):
    # 知乎登录
    if re.match('^1\d{10}', account):
        print('手机号码登录')
        post_url = 'https://www.zhihu.com/login/phone_num'


def get_cookie():
    cookies = '_zap=c2afa24c-a679-4754-98d2-6fed837907c8; d_c0="ADBvowXJZRCPTnOzD4YWmTXqwkhnoqy1aXU=|1574488598"; _xsrf=BW1rYmucj4ERYo8mvNaQyptwTC1CXPhL; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581320229,1581320397,1581320406,1581402226; l_n_c=1; l_cap_id="YTAzODZiZTVkM2FlNGU1YzkxZWE0YzljZTg2ZTA4OTY=|1581402899|3ad84fe2b1098cd615a3ad46b9a53a6bff39cce0"; r_cap_id="NDVkZDY2OWFkYTMzNDAwNDk0Zjk5Yzc5YTllMDA4YmU=|1581402899|188c053977323b465cda95770e434f986ee8152b"; cap_id="YmNiMjAzZWIyMGZiNGE5ZmI2MDlmYzJhN2M0NjdmNjk=|1581402899|9925db0bd02269c2ce6bd30a3ae27d899f67b299"; n_c=1; capsion_ticket="2|1:0|10:1581403683|14:capsion_ticket|44:MTZhZmE4NGI4Zjc1NGUyZWE3OTk0MDNkZjYzM2U5Y2Y=|ffd4520898915ca8f6941e09c2b7a3256c90fd0bb5c5815d1764231915d1069d"; z_c0="2|1:0|10:1581403689|4:z_c0|92:Mi4xTDdzM0F3QUFBQUFBTUctakJjbGxFQ1lBQUFCZ0FsVk5LWnd2WHdCNF8yM1hHclUwYWVMa1hhRDdLU05mblBrYUxn|8578e8e905a10c8f6998b0daad92f585acd012899ae8d451ebb27e8306e9ded5"; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581403692; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1581403692|1581402225'
    line = cookies.split('; ')
    cookie = {}
    for i in line:
        key, value = i.split('=', 1)
        cookie[key] = value
    return cookie


cookies = get_cookie()

user_agent = UserAgent()

headers = {
    'HOST': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/signin?next=%2F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

resp = requests.get('https://www.zhihu.com/question/319589443/answer/969924950', cookies=cookies, headers=headers)
# print(resp.content.decode('utf-8'))

sel = Selector(text=resp.content.decode('utf-8'))
article = sel.xpath("//div[@class='RichContent RichContent--unescapable']/div[@class='RichContent-inner']/span//*[name(.)!='a']/text()").extract()
if article:
    print(''.join(article).strip())
pass