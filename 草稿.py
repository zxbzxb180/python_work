import requests
from fake_useragent import UserAgent

useragent = UserAgent()
headers = {
    'User-Agent': useragent.random
}

res = requests.get("https://bbs.csdn.net/forums/ios").content.decode('utf-8')

print(res)