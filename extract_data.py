#!/usr/bin/python
# -*- coding:utf8 -*-
import jieba
from crawl_data import Crawl
from collections import Counter
import db
# jieba.load_userdict("person_name.txt")

class StatNameFreq:
    """
    提取原始数据中的人物名字出现词频
    输入：namelist,text
    """
    @staticmethod
    def static(namelist, text):
        result = [0] * len(namelist)
        seg_list = jieba.cut(text)
        # print("seg_list=>", list(seg_list))
        c = Counter()
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1
        for k, v in c.items():
            if k in namelist:
                num = namelist.index(k)
                result[num] = result[num] + v
            else:
                continue
        return result

def get_name():
    namelist = []
    op = db.OperateMySQL()
    op.connection()
    sql = "select * from jingyong.character"
    re = op.select(sql)
    for row in re:
        namelist.append(row[1].strip(" "))
    return namelist

if __name__ == "__main__":
    URL = "http://www.jinyongwang.com/fei/"
    URL_ID = 0
    URL_Base = "http://www.jinyongwang.com"
    namelist = get_name()
    crawl = Crawl(URL, URL_ID, URL_Base)
    crawl.OpenSeeion()
    import numpy as np
    result_array = np.zeros(shape=(len(namelist), ), dtype="int32")
    for path in crawl.listpath: # 所有章节链接
        text_list = crawl.gettext(path) # 每章节所有段落
        for text in text_list:
            result = StatNameFreq.static(namelist, text)
            result_array += np.array(result)
    print({namelist[i]: result_array[i] for i in range(len(namelist))})
    print("核心人物：", namelist[np.argmax(result_array)])
    







