import baostock as bs
import pandas as pd

from datetime import datetime, timedelta


def stock_index(code, fields, start_date, end_date, frequency):
    # 登陆系统
    # lg = bs.login()

    # 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
    # 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
    # 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
    # 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
    # 二级行业指数，例如：sh.000952 300 地产，sz.399951 300 银行 等；
    # 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
    # 成长指数，例如：sz.399376 小盘成长 等；
    # 价值指数，例如：sh.000029 180 价值 等；
    # 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

    # 详细指标参数，参见“历史行情指标参数”章节；“周月线”参数与“日线”参数不同。
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    rs = bs.query_history_k_data_plus(
        code=code,
        fields=fields,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency
    )

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    # 登出系统
    # bs.logout()

    return result


def code_index(code, num_month):
    """ 输入代码，返回指数 """
    # 获取当前日期
    current_date = datetime.now()

    # 计算6个月前的日期
    six_months_ago = current_date - timedelta(days=num_month * 30)  # 这里简化计算，每个月按30天计算

    # 转换格式
    current_date = current_date.strftime('%Y-%m-%d')
    six_months_ago = six_months_ago.strftime('%Y-%m-%d')

    res = stock_index(
        code=code,
        fields='date, close',
        start_date=six_months_ago,
        end_date=current_date,
        frequency='d',
    )

    return res
