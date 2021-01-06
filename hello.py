#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type','text/plain')]    
    body = ''
    d = parse_qs(environ['QUERY_STRING'])
    for item in d:
    	body += str(item) + "=" + str(d[item]) + "\n"
    start_response (status, headers)
    return [body]
