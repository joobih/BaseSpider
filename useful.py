#!/usr/bin/env python
# coding=utf-8

import re  
from urlparse import urlparse


"""
    将url字符串参数进行检查,是否是合法的url字符串,True代表是,False代表否
"""
def is_normal_url(url):      
    if re.match(r'^https?:/{2}\w.+$', url):  
        return True
    else:  
        return False


"""
    将参数url进行分解,返回使用的协议,主机名,端口号,路径等
"""
def analysis_url(url):
    u = urlparse(url)
    scheme = u.scheme
    hostname = u.hostname
    port = u.port
    path = u.path
    result = {
        "scheme":scheme,
        "hostname":hostname,
        "port":port,
        "path":path
    }
    return result

