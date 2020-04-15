# -*- coding: UTF-8 -*-

import tushare as ts

'''
###############################################################################################################
    指数数据
        获取指数相关数据，为用户提供包括成分、权重和行情在内的数据。目前已经发布的数据如下：
        
        指数基本信息
        指数日线行情
        指数成分和权重数据
###############################################################################################################
'''
pro = ts.pro_api("e9e0569e1db5327f6668ae9e623858cad66b7d3e0a09c138c3afd551")


'''
###############################################################################################################
    指数基本信息:
        接口：index_basic
        描述：获取指数基础信息。
        输入参数：
            market	str	Y	交易所或服务商
            publisher	str	N	发布商
            category	str	N	指数类别
        输出参数：
            ts_code	str	TS代码
            name	str	简称
            fullname	str	指数全称
            market	str	市场
            publisher	str	发布方
            index_type	str	指数风格
            category	str	指数类别
            base_date	str	基期
            base_point	float	基点
            list_date	str	发布日期
            weight_rule	str	加权方式
            desc	str	描述
            exp_date	str	终止日期
        市场说明(market):
            MSCI	MSCI指数
            CSI	中证指数
            SSE	上交所指数
            SZSE	深交所指数
            CICC	中金指数
            SW	申万指数
            OTH	其他指数
###############################################################################################################
'''
def index_basic(market):
    return pro.index_basic(market=market)

