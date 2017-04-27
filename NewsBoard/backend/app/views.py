# -*- coding: utf-8 -*-

from app import app, api
from flask import jsonify
from flask_restful import Resource

import requests
import json
import ast
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
}


class SegmentFault(Resource):

    def get(self):
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

        return jsonify(data=data)
        

api.add_resource(SegmentFault, '/segmentfault')


