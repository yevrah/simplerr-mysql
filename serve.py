#!/usr/bin/env python

import sys
sys.path.append('./website/')

import config

from simplerr import dispatcher

def connect(request):
    config.DATABASE.connect()


def close(request, response):
    config.DATABASE.close()


def create(site='./website', hostname='127.0.0.1', port=3000, reloader=True, debugger=True, evalex=True, processes=1, cache=False):
    wsgi = dispatcher.wsgi(site, hostname, port,
                           use_reloader=reloader,
                           use_debugger=debugger,
                           use_evalex=evalex,
                           threaded=True,
                           processes=processes)

    wsgi.global_events.on_pre_response(connect)
    wsgi.global_events.on_post_response(close)

    return wsgi


app = create()
app.serve()
