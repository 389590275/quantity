# -*- coding：utf-8
# @Time   :2024/7/16 17:08
# @Author :ghostgril
# @Email  :1690085531@qq.com
# @File   :app.py

import fund_util
from src.quantity.utils import util


def any_funds():
    ret_path = "../../../data/ret.txt"
    util.clear_file(ret_path)

    all_funds = []
    lines = util.read_file_by_line("../../../data/fund_hold.txt")
    for line in lines:
        line_arr = str.split(line, " ")
        if len(line_arr) != 2:
            print("读取数据错误", line)
            continue
        all_funds.append(line_arr)

    util.append_line_to_file(ret_path, util.get_now_date())
    util.append_line_to_file(ret_path, "")
    util.append_line_to_file(ret_path, "")

    for fund in all_funds:
        detail, valuation = fund_util.fund_detail(fund[1])
        util.append_line_to_file(ret_path, fund[0] + " " + fund[1])
        util.append_line_to_file(ret_path, "估值: " + str(valuation))
        util.append_line_to_file(ret_path, str(detail))
        util.append_line_to_file(ret_path, "")
        util.append_line_to_file(ret_path, "")


if __name__ == '__main__':
    any_funds()
    # fund_util.fund_detail('008481')
    # fund.fund_detail('012709')
    # s = ak.stock_individual_info_em(symbol="00836")
    # print(s)
