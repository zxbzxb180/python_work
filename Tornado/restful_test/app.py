import tornado.web
import tornado.ioloop
from handlers import user
import tornado.httpserver


HANDLERS = [
    (r'/api/users', user.UserListHandler),
    (r'/api/users/(\d+)', user.UserHandler),

]

def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()