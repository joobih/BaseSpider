#!/usr/bin/env python
# coding=utf-8


import time
from threading import Thread
from my_celery import pic_get
import requests
import base64

url = "https://t1.27270.com/uploads/tu/201702/176/3dtyk3jvmtm.jpg"

#1.同步的方式获取30次图片27s
"""
print time.time()
a = time.time()
for i in range(30):
    r = requests.get(url)
    html = r.content
    html = base64.b64encode(html)
    print html[:10]
b = time.time()
print b-a

"""

#2.celery的方式开启30个线程获取30次图片11s
"""
a = time.time()
print a
def get_pic():
    result = pic_get.delay(url)
    while True:
        if result.ready():
            html = result.get()
#            print "thread",html
            break
        else:
            print "wait..."
        time.sleep(1)

threads = []
for i in range(30):
    t = Thread(target = get_pic)
    threads.append(t)
    
for i in range(30):
    threads[i].start()

for i in range(30):
    threads[i].join()

b = time.time()
print b-a
"""

    

