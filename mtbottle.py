'''Multithreading Bottle server adapter.'''

import bottle
import mtwsgi

class MTServer(bottle.ServerAdapter):
    def run(self, handler):
        thread_count = self.options.pop('thread_count', None)
        server = mtwsgi.make_server(self.host, self.port, handler, thread_count, **self.options)
        server.serve_forever()



if __name__ == '__main__':
    import bottle
    import time

    app = bottle.Bottle()

    @app.route('/')
    def foo():
        time.sleep(1)
        return 'hello, world!\n'

    app.run(server=MTServer, thread_count=2)
    #app.run()
    #httpd = mtwsgi.make_server('0.0.0.0', 8080, app, 3)
    #httpd.serve_forever()

