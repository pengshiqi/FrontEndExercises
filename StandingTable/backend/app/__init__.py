# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app, send_wildcard=True)
api = Api(app, prefix='/api')

from app import views
