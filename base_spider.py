#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append("submodule/Common")

import requests
import useful

class BaseSpider(object):

    def __init__(self,url,**kwag):
        self.url = url
        self.s = requests.Session()
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

        self.proxies = None

    """
        打开爬虫入口页面
    """
    def index(self):
        r = self.s.get(self.url,headers = self.headers)
        html = r.content
        return html

    """
        解析页面中的重要数据
    """
    def parser_data(self,html):
        raise NotImplementedError

    """
        解析页面中的url
    """
    def parser_url(self,html):
        raise NotImplementedError

    def run(self):
        html = self.index()
        urls = self.parser_url(html)
        result = []
        for u in urls:
            r = self.s.get(u,headers = self.headers)
            h = r.content
            data = self.parser_data(h)
            if data:
                result.extend(data)

        return result
