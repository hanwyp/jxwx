import time, datetime
import os
import sqlite3
import test

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = os.getcwd() + "\\jxphone.db"
engine = create_engine('sqlite:///jxphone.db?check_same_thread=False', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Br(Base):
    __tablename__ = 'br'
    brID = Column(Integer, primary_key=True)
    brName = Column(String(20))

    def __repr__(self):
        return "<Br(id='%s',brName='%s')>" % ( \
            self.brID, self.brName)

    def br_list(self):
        session = Session()
        user = session.query(Br)
        dic_temp = []
        for u in user:
            dic_temp.append(u.brName)
        return dic_temp


class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    brID = Column(Integer)
    phName = Column(String(20))

    def __repr__(self):
        return "<Br(id='%s',brID='%s',phName='%s')>" % ( \
            self.id, self.brID, self.phName)


class PhEdit(Base):
    __tablename__ = 'phEdit'
    id = Column(Integer, primary_key=True)
    phID = Column(Integer)
    guzhang = Column(String(100))
    rq = Column(String)
    jiage = Column(Integer)
    baoxiu = Column(String(10))
    gkID = Column(Integer)
    phedit = Column(String(100))

    def __repr__(self):
        return f"<Br(id='{self.id}',phID='{self.phID}',guzhang='{self.guzhang}',rq={self.rq},jiage='{self.jiage}',baoxiu='{self.baoxiu}',gkID='{self.gkID}',PersonID='{self.PersonID}',phedit='{self.phedit}')>"


class EditPs(Base):
    __tablename__ = 'editPs'
    id = Column(Integer, primary_key=True)
    Name = Column(String)

    def __repr__(self):
        return f"<EditPs(id='{self.id}',Name='{self.Name}')>"


class Guke(Base):
    __tablename__ = 'guke'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    dianhua = Column(String)
    sex = Column(String)


if __name__ == '__main__':
    pass

    # br_list = Br()
    # print(br_list.br_list())

    # Session=sessionmaker(bind=engine)
    # session = Session()
    #
    # user = session.query(EditPs)
    # list_temp=[]
    # for u in user:
    #     list_temp.append(u.Name)
    # print(list_temp)

    # edit_ps=EditPs()
    # edit_ps.Name='不充电'
    # session.add(edit_ps)
    # session.commit()

    # phEdit表操作
    # ph_edit=PhEdit()
    # ph_edit.id=test.dan_hao()
    # ph_edit.phID=14
    # ph_edit.guzhang='不显示'
    # ph_edit.rq='2020-08-12'
    # ph_edit.jiage=180
    # ph_edit.baoxiu='一个月'
    # ph_edit.gkID=1
    # ph_edit.PersonID=1
    # ph_edit.phedit='更换屏幕'
    # print(ph_edit)
    # session.add(ph_edit)
    # session.commit()

    # our_user=session.query(Br).filter_by(brName='亿通').first()
    # our_br=Br()
    # our_br.brName="黑鲨"
    # session.add(our_br)

    # our_phone=Phone()
    # our_phone.brID=3
    # our_phone.phName='S6'
    # print(our_phone)
    # session.add(our_phone)
    # session.commit()
