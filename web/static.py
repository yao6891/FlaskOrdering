#!/usr/bin/ python
# -*- coding: utf-8 -*-
__author__ = 'mtianyan'
__date__ = '2018-11-27 18:16'
from flask import Blueprint, send_from_directory
from application import app

"""
            　┏┓　　　┏┓+ +
  　　　　　　　┏┛┻━━━┛┻┓ + +
  　　　　　　　┃　　　　　　　┃ 　
  　　　　　　　┃　　　━　　　┃ ++ + + +
  　　　　　　 ████━████ ┃+
  　　　　　　　┃　　　　　　　┃ +
  　　　　　　　┃　　　┻　　　┃
  　　　　　　　┃　　　　　　　┃ + +
  　　　　　　　┗━┓　　　┏━┛
  　　　　　　　　　┃　　　┃　　　　　　　　　　　
  　　　　　　　　　┃　　　┃ + + + +
  　　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
  　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
  　　　　　　　　　┃　　　┃
  　　　　　　　　　┃　　　┃　　+　　　　　　　　　
  　　　　　　　　　┃　 　　┗━━━┓ + +
  　　　　　　　　　┃ 　　　　　　　┣┓
  　　　　　　　　　┃ 　　　　　　　┏┛
  　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
  　　　　　　　　　　┃┫┫　┃┫┫
  　　　　　　　　　　┗┻┛　┗┻┛+ + + +
"""

route_static = Blueprint('static', __name__)


@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)
