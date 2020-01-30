import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web
import time

class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(3)
        yield tornado.gen.sleep(3)
        self.write('when i sleep?')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/sleep", SleepHandler),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print('server start on 8888')
    tornado.ioloop.IOLoop.current().start()
