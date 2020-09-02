# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Br(Base):
    __tablename__ = 'br'

    brID = Column(Integer, primary_key=True)
    brName = Column(Text)


class EditP(Base):
    __tablename__ = 'editPs'

    id = Column(Integer, primary_key=True)
    Name = Column(Text)


class Guke(Base):
    __tablename__ = 'guke'

    id = Column(Integer, primary_key=True)
    Name = Column(Text)
    dianhua = Column(Text)
    sex = Column(Boolean)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True, unique=True)
    brID = Column(ForeignKey('br.brID'))
    phName = Column(Text)

    br = relationship('Br')


class PhEdit(Base):
    __tablename__ = 'phEdit'

    id = Column(Integer, primary_key=True)
    phID = Column(ForeignKey('phone.id'))
    guzhang = Column(Text)
    rq = Column(Text)
    jiage = Column(Integer)
    baoxiu = Column(Text)
    gkID = Column(ForeignKey('guke.id'))
    phedit = Column(Text)

    guke = relationship('Guke')
    phone = relationship('Phone')
