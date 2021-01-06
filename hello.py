#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):   
    body = ""
    d = environ['QUERY_STRING'].strip().split('&')
    for i in d:
    	body += str(i) + '\n'
    body.strip()
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(bytes(body,'ascii'))))
        ])
    print(environ['QUERY_STRING'], "\n\n\n", d, "\n\n\n", body)
    return iter([bytes(body,'ascii')])
