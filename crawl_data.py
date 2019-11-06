#!/usr/bin/python
# -*- coding:utf8 -*-
import urllib3
from bs4 import BeautifulSoup
import lxml
import  re
import os


class Crawl:
    """
    爬取原始数据
    URL_Base: http://www.jinyongwang.com
    URL: http://www.jinyongwang.com/fei/
    URL_ID: 0-15
    """
    def	__init__(self, URL, URL_ID, URL_Base):#构造函数参数分别为小说网址链接、小说编号（1~15）、网站链接；
        self.URL = URL
        self.URL_ID = URL_ID
        self.URL_Base = URL_Base
        self.listpath = None
    
    def	OpenSeeion(self):#获取小说所有章节链接；
        try:
            respond = urllib3.PoolManager().request('GET', self.URL)
            html = respond.data
            soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
            OringialPath = soup.find_all(class_="mlist")
            pattern = re.compile('(?<=href=").*?(?=")')
			#print str(OringialPath)
            self.listpath =  re.findall(pattern,str(OringialPath) )
        except:
            print("Error")

    def	gettext(self, sessionURL):#获取该章节所有段落，返回数据类型为List
        web = self.URL_Base + sessionURL
        respond = urllib3.PoolManager().request('GET', web)
        html = respond.data.decode('utf-8')
        pattern = re.compile('(?<=<p>).*?(?=</p>)')
        text = re.findall(pattern, str(html) )
        return text


if __name__ == "__main__":
    URL = "http://www.jinyongwang.com/fei/"
    URL_ID = 0
    URL_Base = "http://www.jinyongwang.com"
    crawl = Crawl(URL, URL_ID, URL_Base)
    crawl.OpenSeeion()
    for path in crawl.listpath:
        text = crawl.gettext(path)
        print(text)