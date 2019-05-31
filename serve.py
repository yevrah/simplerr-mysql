#!/usr/bin/env python

import sys
sys.path.append('./website/')

from config import DB
from simplerr import dispatcher

def connect(request):
    DB.connect()

def close(request, response):
    DB.close()

def create(site='./website', hostname='127.0.0.1', port=3000):
    wsgi = dispatcher.wsgi(site, hostname, port,)
    wsgi.global_events.on_pre_response(connect)
    wsgi.global_events.on_post_response(close)
    return wsgi

app = create()
app.serve()
