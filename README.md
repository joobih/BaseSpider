# CSpider
爬虫基础类,使用requests库.抓取网站通用类

##CSpider 成员方法

###parser_data

    该方法主要是解析页面的重要数据,子类自行重写定制该方法,提取出自己所需要的数据

###index

    该方法是网站的入口,参数为网站首页地址

###parser_url(self,html)

    该方法是解析出html页面中包含重要数据的所有url地址的列表


