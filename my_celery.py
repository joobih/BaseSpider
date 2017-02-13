#!/usr/bin/env python
# coding=utf-8

from celery import Celery
import requests

from headers import HEADERS
import base64

app = Celery("tasks",broker='amqp://guest@localhost//',backend='redis://localhost')

@app.task
def pic_get(url,cookies = None):
    try:
        r = requests.get(url,cookies = cookies,headers = HEADERS)
        html = r.content
        html = base64.b64encode(html)
        return html
    except Exception,e:
        print "my_get for celery occure a Exception:{}".format(e)
        return None
