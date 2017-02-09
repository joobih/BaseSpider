#!/usr/bin/env python
# coding=utf-8

import requests
import json
import time

from headers import HEADERS


def proxy_check(ip,port,type = "http"):
    try:
        result = {}
        url = "http://httpbin.org/ip"
        start_time = time.time()
        proxy = {
            type:"{}://{}:{}".format(type,ip,port)
        }
        print proxy,"proxy"
        r = requests.get(url,headers = HEADERS,proxies = proxy,timeout = 10)
        end_time = time.time()
        html = r.content
        result["is_available"] = False
        j_res = json.loads(html)
        if ip == j_res["origin"]:
            result["is_available"] = True
            result["respond_speed"] = end_time - start_time
        return result
    except Exception,e:
        print "proxy_check Exception:{}".format(e)
        return None

ip = "118.123.245.154"
port = "3128"

print proxy_check(ip,port)
