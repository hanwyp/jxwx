from tableModel import *
import sys
import sqlite3
import os

path = os.getcwd() + "\\jxphone.db"
engine = create_engine('sqlite:///jxphone.db?check_same_thread=False', echo=False)
Session = sessionmaker(bind=engine)


# 返回表中的一列的所有值（列表）
def date_all(class_name, num, str_name):
    session = Session()
    user = session.query(class_name).all()
    dic_temp = {}
    list_temp = []
    for u in user:
        dic_temp[eval('u.' + num)] = eval('u.' + str_name)
        list_temp.append(eval('u.' + str_name))
    return dic_temp, list_temp

# 返回表中的一列的所有值（列表）

def date_select(class_name, num, str_name,filterStr):
    session = Session()
    print(filterStr)
    user = session.query(class_name).filter(eval(filterStr)).all()
    dic_temp = {}
    list_temp = []
    for u in user:
        dic_temp[eval('u.' + num)] = eval('u.' + str_name)
        list_temp.append(eval('u.' + str_name))
    return dic_temp, list_temp

# 查找是否已经存在
def checks(class_name, filterStr):
    session = Session()
    # print(filterStr)
    user = session.query(class_name).filter(eval('Br.brName=="'+filterStr.upper()+'"')).all()
    # print(len(user))
    return len(user)



if __name__ == '__main__':
    # print(date_br(Br, 'brID','brName'))
    # print(date_select(Phone,'id','phName','Phone.brID==2')[0])
    # print(date_select(Phone, 'id', 'phName', 'brID==2')[0])
    print(checks(Br, "opp".upper()))
    # print('oppo'.upper())