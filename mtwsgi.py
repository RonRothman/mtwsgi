'''WSGI-compliant HTTP server.  Dispatches requests to a pool of threads.'''

from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
import multiprocessing.pool

__all__ = ['ThreadPoolWSGIServer', 'make_server']



class ThreadPoolWSGIServer(WSGIServer):
    '''WSGI-compliant HTTP server.  Dispatches requests to a pool of threads.'''

    def __init__(self, thread_count=None, *args, **kwargs):
        '''If 'thread_count' == None, we'll use multiprocessing.cpu_count() threads.'''
        WSGIServer.__init__(self, *args, **kwargs)
        self.thread_count = thread_count
        self.pool = multiprocessing.pool.ThreadPool(self.thread_count)

    # Inspired by SocketServer.ThreadingMixIn.
    def process_request_thread(self, request, client_address):
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        self.pool.apply_async(self.process_request_thread, args=(request, client_address))


def make_server(host, port, app, thread_count=None, handler_class=WSGIRequestHandler):
    '''Create a new WSGI server listening on `host` and `port` for `app`'''
    httpd = ThreadPoolWSGIServer(thread_count, (host, port), handler_class)
    httpd.set_app(app)
    return httpd



if __name__ == '__main__':
    from wsgiref.simple_server import demo_app
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    import webbrowser
    webbrowser.open('http://localhost:8000/xyz?abc')
    httpd.serve_forever()

