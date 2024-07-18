import tushare as ts

# 设置你的Tushare API令牌
ts.set_token('xxx')
# 初始化pro接口
pro = ts.pro_api()


# # 获取某个股票的历史数据，例如平安银行（股票代码000001.SZ）
# df = pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20230101')
#
# # 显示前几行数据
# print(df.head())

def get_stock_chg_tushare(code):
    # 东财数据
    df = ts.realtime_quote(ts_code=code+'.HK', src='dc')
    print(df)
    return 0


if __name__ == '__main__':
    get_stock_chg_tushare('01071')
