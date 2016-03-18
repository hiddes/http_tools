# --coding:utf8 -- #
import tornado
import tornado.httpserver
import tornado.ioloop
from tornado.web import Application, RequestHandler


class Index(RequestHandler):
    def get(self):
        print self.request.arguments
        self.write('get ok')

    def post(self):
        # print self.request.body
        print self.request.cookies
        self.write('post ok')

    def options(self, *args, **kwargs):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Credentials', True)
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type, *')


class JS(RequestHandler):
    def get(self):
        js = 'test.js'
        print 'load js'
        self.render(js)


def main():
    app = Application(
            [('/', Index),
             ('/js', JS)]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(7000)
    print 'listening the port:7000'
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
