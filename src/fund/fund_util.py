# -*- coding：utf-8
# @Time   :2024/7/15 20:13
# @Author :ghostgril
# @Email  :1690085531@qq.com
# @File   :fund_util.py

import akshare as ak
import pandas as pd

import stock_util


# 获取基金持仓详情
def fund_detail(fund_code):
    temp_df = ak.fund_portfolio_hold_em(fund_code)
    chgs = []
    for code in temp_df["股票代码"]:
        chg = stock_util.get_stock_chg(code)
        chgs.append(chg)
    temp_df["涨跌幅（%）"] = pd.array(chgs)

    fund_chgs = []

    fund_chg_sum = 0

    arr_1 = temp_df.get('占净值比例')
    arr_2 = temp_df.get('涨跌幅（%）')

    for i in range(0, len(arr_1)):
        rate = arr_1[i]
        chg = arr_2[i]
        pd.isnull(chg)
        if pd.isnull(chg):
            chg = 0
        fund_chg = float(rate) * float(chg) / 100
        fund_chgs.append(fund_chg)
        fund_chg_sum = fund_chg_sum + fund_chg

    temp_df["贡献（%）"] = pd.array(fund_chgs)

    temp_df = temp_df[
        [
            "股票代码",
            "股票名称",
            "持股数",
            "持仓市值",
            "涨跌幅（%）",
            "占净值比例",
            "贡献（%）",
        ]
    ]
    print(temp_df)
    print("估值", str(fund_chg_sum) + "%")
    return temp_df, fund_chg_sum


if __name__ == '__main__':
    fund_detail('008481')
