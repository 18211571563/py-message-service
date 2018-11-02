# -*- coding: UTF-8 -*-

import json

from flask import Flask, Response

import tushare_data_service as ts

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


app.run(port=3000, host='0.0.0.0');