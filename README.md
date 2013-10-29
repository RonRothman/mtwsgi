mtwsgi
======

Multithreaded Python WSGI implementation.

Drop-in replacement for wsgiref.WSGIServer, but dispatches
requests to threads in a pool instead of serving requests
serially (blocking).

Can be used indepently of [Bottle](http://bottlepy.org/), but here's an example that uses both:

    import bottle
    import time

    app = bottle.Bottle()

    @app.route('/')
    def foo():
        time.sleep(2)
        return 'hello, world!\n'

    app.run(server=MTServer, host='0.0.0.0', port=8080, thread_count=3)
