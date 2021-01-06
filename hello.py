#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):   
    body = b""
    d = parse_qs(environ['QUERY_STRING'])
    body = [bytes(str(i) + '=' + str(d[i]) + '\n', 'ascii') for i in d]
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(body)))
        ])
    print()
    return body
