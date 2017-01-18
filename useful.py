#!/usr/bin/env python
# coding=utf-8

import re  
import hashlib
import uuid
from urlparse import urlparse
from datetime import datetime

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


"""
    如果你想要一个完全不同的文件名不妨试试它,传入一个想要的文件类型
"""
def get_file_name(file_type):
    uid = uuid.uuid4()
    t = datetime.now()
    t = str(t)
    t = t[:19]
    file_name = t + "_" + str(uid)
    file_name = file_name.replace(" ","_").replace(".","_").replace(":","_").replace("-","_") + ".{type_}".format(type_ = file_type)
    db_file = file_name
    file_name = setting.SERVER_PATH + file_name
    return db_file,file_name


"""
    将data字符串的数据转换为md5字符串
"""
def get_md5(data):
    m2 = hashlib.md5()
    m2.update(data)
    md5_str = m2.hexdigest()
    return md5_str

