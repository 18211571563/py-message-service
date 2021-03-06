# -*- coding: UTF-8 -*-

import tushare as ts


'''
###############################################################################################################
    基础数据
        提供交易和回测所需要的基础信息，目前主要提供的是上市公司股票列表和交易日历等

        股票列表
        各交易所交易日历
        沪深股通成份股
        股票曾用名
        上市公司基本信息
        IPO新股列表
###############################################################################################################
'''
pro = ts.pro_api("e9e0569e1db5327f6668ae9e623858cad66b7d3e0a09c138c3afd551")

'''
###############################################################################################################
    股票列表:
        接口：stock_basic
        描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
        输入参数：
            is_hs		是否沪深港通标的，N否 H沪股通 S深股通
            list_status		上市状态： L上市 D退市 P暂停上市
            exchange		交易所 SSE上交所 SZSE深交所 HKEX港交所
###############################################################################################################
'''
def stock_basic():
    return pro.stock_basic(exchange_id='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')


'''
###############################################################################################################
    交易日历:
        接口：trade_cal
        描述：获取各大交易所交易日历数据,默认提取的是上交所
        输入参数：
            exchange		交易所 SSE上交所 SZSE深交所
            start_date		开始日期
            end_date		结束日期
            is_open	int	N	是否交易 0休市 1交易
        输出参数:
            exchange	    str	Y	交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源,IB 银行间,XHKG 港交所
            cal_date	    str	Y	日历日期
            is_open	        str	Y	是否交易 0休市 1交易
            pretrade_date	str	N	上一个交易日
###############################################################################################################
'''
def trade_cal(exchange = '', start_date = '', end_date = ''):
    return pro.trade_cal(exchange=  exchange, start_date= start_date, end_date= end_date);


'''
###############################################################################################################
    上市公司基本信息:
        接口：stock_company
        描述：获取上市公司基础信息
        积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法
        输入参数：
            exchange		交易所代码 ，SSE上交所 SZSE深交所 ，默认SSE
###############################################################################################################
'''
def stock_company():
    return pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province');


'''
###############################################################################################################
    沪深股通成份股:
        接口：hs_const
        描述：获取沪股通、深股通成分数据
        输入参数：
            hs_type		类型SH沪股通SZ深股通
            is_new		是否最新 1 是 0 否 (默认1)
###############################################################################################################
'''
def hs_const():
    return pro.hs_const(hs_type='SH');

'''
###############################################################################################################
    股票曾用名:
        接口：namechange
        描述：历史名称变更记录
        输入参数：
            ts_code		TS代码
            start_date		公告开始日期
            end_date		公告结束日期
###############################################################################################################
'''
def namechange(ts_code):
    return pro.namechange(ts_code=ts_code, fields='ts_code,name,start_date,end_date,change_reason')


'''
###############################################################################################################
    IPO新股列表:
        接口：new_share
        描述：获取新股上市列表数据
        限量：单次最大2000条，总量不限制
        积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法
        输入参数：
            start_date		上网发行开始日期
            end_date		上网发行结束日期
###############################################################################################################
'''
def new_share():
    return pro.new_share()

'''
###############################################################################################################
    日线行情
        接口：daily
        数据说明：交易日每天15点～16点之间。本接口是未复权行情，停牌期间不提供数据。
        调取说明：基础积分每分钟内最多调取200次，每次4000条数据，相当于超过18年历史，用户获得超过5000积分无频次限制。
        描述：获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据。
        输入参数：
            ts_code		    股票代码（二选一）
            trade_date		交易日期（二选一）
            start_date		开始日期(YYYYMMDD)
            end_date		结束日期(YYYYMMDD)

        输出参数：
            ts_code	str	    股票代码
            trade_date	str	交易日期
            open	float	开盘价
            high	float	最高价
            low	float	    最低价
            close	float	收盘价
            pre_close	float	昨收价
            change	float	涨跌额
            pct_chg	float	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
            vol	float	    成交量 （手）
            amount	float	成交额 （千元）


###############################################################################################################
'''
def daily(ts_code, start_date, end_date):
    return pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)

'''
###############################################################################################################
    通用行情接口
        接口：pro_bar
        
###############################################################################################################
'''
def pro_bar(asset ,ts_code, start_date, end_date):
    df = ts.pro_bar(asset=asset, api=pro, ts_code=ts_code, adj='qfq', start_date=start_date, end_date=end_date)
    return df