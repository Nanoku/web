#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):   
    body = []
    d = parse_qs(environ['QUERY_STRING'])
    for i in d:
    	for it in d[i]:
            body.append(bytes(str(i) + '=' + str(it), 'ascii'))
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(body)))
        ])
    print()
    return [body]
