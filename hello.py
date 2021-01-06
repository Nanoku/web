#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):   
    body = b""
    d = parse_qs(environ['QUERY_STRING'])
    for item in d:
    	body += str(item) + "=" + str(d[item]) + "\n"
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
    return iter([body])
