#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
    #бизнес-логика
    status = '200 OK'
    headers = [('Content-Type','text/plain')]    
    body = ''
    d = parse_qs(environ['QUERY_STRING'])
    for item in d:
    	body += item + "=" + d[item]
    start_response (status, headers)
    return [body]