# -*- coding: utf-8 -*-
"""
    This is the python script to update data in mysql.
"""

import time
import requests
import json
from bs4 import BeautifulSoup

# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
}

t = time.localtime()
date_num = int('{}{:0>2d}{:0>2d}'.format(t[0], t[1], t[2]))

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class SegmentFault(Base):
    # 表的名字:
    __tablename__ = 'SegmentFault'

    # 表的结构:
    id = Column(Integer, primary_key=True, nullable=False)
    author = Column(String(100), nullable=False)
    comments_number = Column(Integer, nullable=False)
    favour_number = Column(Integer, nullable=False)
    link = Column(String(100), nullable=False)
    tag = Column(String(20), nullable=False)
    title = Column(String(200), nullable=False)
    date = Column(Integer, nullable=False)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/NewsBoard')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# Crawl Data
url = 'https://segmentfault.com/news'
        
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

news_item = soup.select('.news__item')

data = []

for item in news_item:
    temp_data = dict()
    temp_data['favour_number'] = item.select('.news__item-zan-number')[0].get_text()
    temp_data['comments_number'] = item.select('.news__item-comment-box')[0].get_text()
    temp_data['title'] = item.select('.mr10')[0].get_text()
    temp_data['author'] = item.select('.mr10')[1].get_text()
    temp_data['tag'] = item.select('.ml10')[0].get_text()
    temp_data['link'] = 'https://segmentfault.com' + item.select('.news__item-external-link')[0]['href']
    
    data.append(temp_data)

# print data

for item in data:
    collect = SegmentFault(author=item['author'], comments_number=int(item['comments_number']), favour_number=int(item['favour_number']),
                            link=item['link'], tag=item['tag'], title=item['title'], date=date_num)
    session.add(collect)

# 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()
