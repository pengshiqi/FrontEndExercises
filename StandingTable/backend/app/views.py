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


class StandingTable(Resource):

    def get(self, league):
        url = 'https://soccer.hupu.com/table/{league}.html'.format(league=league)
        
        r = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(r.text, 'lxml')
        
        head = soup.select('#main_table > thead > tr > th')
        head_list = [item.get_text() for item in head]
        
        standing = soup.select('#main_table > tbody > tr')
        data_list = []
        for item in standing:
            d = item.select('td')
            res = dict()
            for i in range(len(d)):
                res[head_list[i]] = d[i].get_text()
            data_list.append(res)

        return jsonify(data=data_list)


class Test(Resource):

    def get(self):
        data = [0] * 6
        data[0] = dict(team_order=1, team_cn=u'切尔西', logo='http://www.sinaimg.cn/lf/sports/logo85/60.png', count='23', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')
        data[1] = dict(team_order=2, team_cn=u'热刺', logo='http://www.sinaimg.cn/lf/sports/logo85/66.png', count='23', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')
        data[2] = dict(team_order=3, team_cn=u'阿森纳', logo='http://www.sinaimg.cn/lf/sports/logo85/61.png', count='23', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')
        data[3] = dict(team_order=4, team_cn=u'利物浦', logo='http://www.sinaimg.cn/lf/sports/logo85/53.png', count='23', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')
        data[4] = dict(team_order=5, team_cn=u'曼城', logo='http://www.sinaimg.cn/lf/sports/logo85/216.png', count='22', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')
        data[5] = dict(team_order=6, team_cn=u'曼联', logo='http://www.sinaimg.cn/lf/sports/logo85/52.png', count='22', score='56', win='18', draw='2', lose='3', goal='48', losegoal='16', truegoal='32')

        return jsonify(data=data)
        

api.add_resource(StandingTable, '/table/<string:league>')
api.add_resource(Test, '/test')

