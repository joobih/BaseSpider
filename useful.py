#!/usr/bin/env python
# coding=utf-8

import urllib
import re  
from urlparse import urlparse
      
#    url = "http://www.baidu.com"  
def is_normal_url(url):      

    if re.match(r'^https?:/{2}\w.+$', url):  
        print("Ok.")  
        return True
    else:  
        print("Error.")  
        return False

def analysis_url(url):
    u = urlparse(url)
    scheme = u.scheme
    print "protocol:",scheme
    hostname = u.hostname
    print "hostname:",hostname
    port = u.port
    print "port:",port
    path = u.path
    print "path:",path
    result = {
        "scheme":scheme,
        "hostname":hostname,
        "port":port,
        "path":path
    }
    return result

url = "http://www.baidu.com"
print is_normal_url(url)
print analysis_url(url)
