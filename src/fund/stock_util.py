# -*- coding：utf-8
# @Time   :2024/7/18 14:41
# @Author :ghostgril
# @Email  :1690085531@qq.com
# @File   :stock_util.py

import akshare as ak

sh_pre = ("6", "5", "9")
h_stocks = None
a_stocks = None


def stock_type(code):
    if len(code) == 5:
        return "HK"
    if len(code) == 6:
        for p in sh_pre:
            if str.startswith(code, p):
                return "SH"
        return "SZ"
    return ""


# H股信息
def get_stock_info_hk(stock_code):
    global h_stocks
    if h_stocks is None:
        h_stocks = ak.stock_hk_spot_em()
    stock = h_stocks[h_stocks['代码'] == stock_code]
    return stock


# A股信息
def get_stock_info_a(stock_code):
    global a_stocks
    if a_stocks is None:
        a_stocks = ak.stock_zh_a_spot_em()
    stock = a_stocks[a_stocks['代码'] == stock_code]
    return stock


# h股 涨跌幅
def get_stock_chg_h(stock_code):
    # 获取股票实时价格
    stock = get_stock_info_hk(stock_code)
    if not stock.empty:
        return float(stock['涨跌幅'].values[0])
    else:
        return None


# a股 涨跌幅
def get_stock_chg_a(stock_code):
    stock = get_stock_info_a(stock_code)
    if not stock.empty:
        return float(stock['涨跌幅'].values[0])
    else:
        return None


def get_stock_chg(code):
    if stock_type(code) == "HK":
        return get_stock_chg_h(code)
    else:
        return get_stock_chg_a(code)


if __name__ == '__main__':
    print(get_stock_chg('000001'))
