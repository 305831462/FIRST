#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid  #Universally Unique Identifier，简称UUID uuid通用唯一识别码 uuid4()——基于随机数

from orm import Model, StringField, BooleanField, FloatField, TextField
import sqlite3

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


def createDB():
    conn = sqlite3.connect('awesome.db')
    cursor = conn.cursor()
    cursor.execute('create table users (id varchar(50) primary key, email varchar(50), passwd varchar(50), admin bool, name varchar(50), image varchar(50), created_at real)')
    cursor.execute('create table blogs (id varchar(50) primary key, user_id varchar(50), user_name varchar(50), user_image varchar(50), name varchar(50), summary varchar(50), content mediumtext, created_at real)')
    cursor.execute('create table comments (id varchar(50) primary key, blog_id varchar(50), user_id varchar(50), user_name varchar(50), user_image varchar(50), content mediumtext, created_at real)')



def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass
