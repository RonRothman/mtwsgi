mtwsgi
======

Multithreaded Python WSGI implementation.

Drop-in replacement for wsgiref.WSGIServer, but dispatches
requests to threads in a pool instead of serving requests
serially (blocking).

