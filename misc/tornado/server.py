import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(''.join([
            '<html>', '<body>', '<form action="/" method="POST">',
            '<input type="text" name="x">', '<input type="text" name="y">',
            '<input type="submit" value="Submit">'
            '</form>', '</body>', '</html>'
        ]))

    def post(self):
        self.set_header("Content-Type", "text/plain")
        x = int(self.get_body_argument("x", 0))
        y = int(self.get_body_argument("y", 0))
        self.write("x + y = {}".format(x + y))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
