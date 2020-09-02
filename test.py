import sqlite3
import os
import time
import random

path = os.getcwd() + "\\jxphone.db"

conn = sqlite3.connect(path)

cursor = conn.cursor()


def brDic(Tab):
    sql = "select * from " + Tab
    cursor.execute(sql)
    br_dic = {}
    for row in cursor:
        # print("ID=",row[0])
        # print("品牌=", row[1])
        br_dic[row[0]] = row[1]
    # print(br_dic)
    #     print(row[0])

    # print(brList)
    cursor.close()

    conn.commit()

    conn.close()

    return br_dic


def selectDic(sql):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(sql)
    ph_dic = {}
    for row in cursor:
        # print("ID=",row[0])
        # print("品牌=", row[1])
        ph_dic[row[0]] = row[1]

        # print(row)
    # print(ph_dic)
    #     print(row[0])

    # print(brList)
    cursor.close()

    conn.commit()

    conn.close()
    # print(ph_dic)
    return ph_dic


def brList(Tab):
    sql = "select * from " + Tab
    cursor.execute(sql)
    # values = cursor.fetchall()
    # val = values[0]
    # print(val)
    br_list = []
    for row in cursor:
        # print("ID=",row[0])
        # print("品牌=", row[1])
        br_list.append(row)

    # print(brList)
    cursor.close()

    conn.commit()

    conn.close()

    return br_list


def selectList(sql, num):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(sql)
    dic_br = {}
    list_br = []
    HtI = 0
    for row in cursor:
        # print(HtI)
        dic_br[HtI] = row
        list_br.append(row[num])
        HtI = HtI + 1
    # print(dic_br)
    # print(list_br)
    return dic_br, list_br


def selectList2(sql):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(sql)
    list = []
    for row in cursor:
        list.append(row)

    return list

def dan_hao():
    localtime = time.localtime(time.time())
    base_code = str(localtime[0]) + str(localtime[1]).zfill(2) + str(localtime[2])+str(localtime[4])
    count_str = str(random.randint(1,9999)).zfill(4)
    oreder = base_code+count_str
    # oreder_list=[]
    # count = 1
    # while True:
    #     if count>100:
    #         break
    #     count_str=str(count).zfill(8)
    #     oreder_list.append(base_code+count_str)
    #     count += 1

    return oreder

def date_now():
    localtime = time.localtime(time.time())
    str_id = "{}-{}-{}".format(str(localtime[0]), str(localtime[1]).zfill(2), str(localtime[2]).zfill(2))
    return str_id

class phoneEdit():
    pass

if __name__ == '__main__':
    # l = brList('br')
    # for lin in l:
    #     print(lin)
    # print(os.getcwd())
    # print(path)

    # dic=brDic("br")
    # # print(dic)
    # sql = "select id,phName from phone where brID='1'"
    # selectDic(sql)
    # sql = "select * from br"
    # selectList(sql)
    print(dan_hao())
