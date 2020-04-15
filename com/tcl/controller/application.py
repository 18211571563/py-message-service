# -*- coding: UTF-8 -*-

import json

from flask import Flask, Response

import basic_data_service as ts
import index_basic_data_service as ibds

'''
    健康心跳
'''
app = Flask(__name__)
@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


'''
    获取股票列表
'''
@app.route("/stock_basic")
def stock_basic():
    data = ts.stock_basic()
    return data.to_json(orient='records').decode("unicode_escape");

'''
    交易日历
'''
@app.route("/trade_cal/<exchange>/<start_date>/<end_date>")
def trade_cal(exchange = '', start_date = '', end_date = ''):
    data = ts.trade_cal(exchange, start_date, end_date)
    return data.to_json(orient='records').decode("unicode_escape");

'''
    上市公司基本信息
'''
@app.route("/stock_company")
def stock_company():
    data = ts.stock_company()
    return data.to_json(orient='records').decode("unicode_escape");

'''
    沪深股通成份股
'''
@app.route("/hs_const")
def hs_const():
    data = ts.hs_const()
    return data.to_json(orient='records').decode("unicode_escape");

'''
    股票曾用名
'''
@app.route("/namechange")
def namechange():
    data = ts.namechange("600848.SH")
    return data.to_json(orient='records').decode("unicode_escape");

'''
    IPO新股列表
'''
@app.route("/new_share")
def new_share():
    data = ts.new_share()
    return data.to_json(orient='records').decode("unicode_escape");

'''
    日线行情
'''
@app.route('/daily/<ts_code>/<start_date>/<end_date>', methods=['GET'])
def daily(ts_code, start_date, end_date):
    data = ts.daily(ts_code, start_date, end_date)
    return data.to_json(orient='records').decode("unicode_escape");


'''
    获取指数基础信息
'''
@app.route("/index_basic/<market>")
def index_basic(market):
    data = ibds.index_basic(market)
    return data.to_json(orient='records').decode("unicode_escape");


'''
    通用行情接口
'''
@app.route('/pro_bar/<asset>/<ts_code>/<start_date>/<end_date>', methods=['GET'])
def pro_bar(asset, ts_code, start_date, end_date):
    data = ts.pro_bar(asset, ts_code, start_date, end_date)
    return data.to_json(orient='records').decode("unicode_escape");




app.run(port=3000, host='0.0.0.0');