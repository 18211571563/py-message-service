# -*- coding: UTF-8 -*-

import tushare as ts

pro = ts.pro_api("e9e0569e1db5327f6668ae9e623858cad66b7d3e0a09c138c3afd551")

'''
    股票列表:
        接口：stock_basic
        描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
'''
def stock_basic():
    return pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

