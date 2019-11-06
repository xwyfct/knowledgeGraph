from extract_data import StatNameFreq, get_name
import json
from crawl_data import Crawl
import db

# create meta table
# URL = "http://www.jinyongwang.com/fei/"
# URL_ID = 0
# URL_Base = "http://www.jinyongwang.com"
# namelist = get_name()
# crawl = Crawl(URL, URL_ID, URL_Base)
# crawl.OpenSeeion()

# op = db.OperateMySQL()
# op.connection()
# for path in crawl.listpath: # 所有章节链接
#     text_list = crawl.gettext(path) # 每章节所有段落
#     for text in text_list:
#         result = StatNameFreq.static(namelist, text)
#         data = []
#         for t in range(len(result)):
#             if result[t] != 0:
#                 dic = {}
#                 dic["ID"] = t+1
#                 dic["num"] = result[t]
#                 data.append(dic)
#         if data:
#             in_json = json.dumps(data)
#             sql = "INSERT INTO jingyong.meta (Dtat) VALUES ('%s');" % str(in_json)
#             re = op.excute(sql)
#             if re == 0:
#                 print("Error")

# creat user relation table
# op = db.OperateMySQL()
# op.connection()
# sql = "select * from jingyong.meta;"
# res = op.select(sql)
# for re in res:
#     dat = re[1]
#     dat = json.loads(dat)
#     if len(dat) > 1:
#         for i in range(len(dat)-1):
#             for j in range(i+1, len(dat)):
#                 source_target = (dat[i]["ID"], dat[j]["ID"])
#                 sql_1 = "select * from jingyong.user_relation where UserID1=%s and UserID2=%s;" % source_target
#                 re_1 = op.select(sql_1)
#                 if re_1:
#                     op.excute("update jingyong.user_relation set num=num+1 where UserID1=%s and UserID2=%s;" % source_target)
#                 else:
#                     op.excute("insert into jingyong.user_relation (UserID1, UserID2, num) values (%s,%s,1);" % source_target)

# creat user relation weight
namelist = get_name()
op = db.OperateMySQL()
op.connection()
res = op.select("select * from jingyong.user_relation")
for re in res:
    source = namelist[re[1]-1]
    target = namelist[re[2]-1]
    weight = re[3]
    op.excute("insert into jingyong.user_relation_weight (Source, Target, weight) values ('%s','%s',%s)" % (source, target, weight))

            