import tornado.gen
import tornado.httpclient
import tornado.ioloop
from tornado import gen
import time
import requests

N = 3
URL = 'http://127.0.0.1:8888/sleep'

@gen.coroutine
def main():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield [
        http_client.fetch(URL) for i in range(N)
    ]

beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print('async', time.time()-beg1)

beg2 = time.time()
for i in range(N):
    requests.get(URL)
print('req', time.time()-beg2)