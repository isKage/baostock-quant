import baostock as bs
import pandas as pd


def sz50():
    # 登陆系统
    # lg = bs.login()

    # 获取上证 50 成分股
    rs = bs.query_sz50_stocks()

    sz50_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        sz50_stocks.append(rs.get_row_data())
    result = pd.DataFrame(sz50_stocks, columns=rs.fields)

    # 登出系统
    bs.logout()

    return result


def hs300():
    # 登陆系统
    lg = bs.login()

    # 获取沪深 300 成分股
    rs = bs.query_hs300_stocks()

    hs300_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        hs300_stocks.append(rs.get_row_data())
    result = pd.DataFrame(hs300_stocks, columns=rs.fields)

    # 登出系统
    bs.logout()

    return result


def zz500():
    # 登陆系统
    lg = bs.login()

    # 获取中证 500 成分股
    rs = bs.query_zz500_stocks()

    zz500_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        zz500_stocks.append(rs.get_row_data())
    result = pd.DataFrame(zz500_stocks, columns=rs.fields)

    # 登出系统
    # bs.logout()

    return result


if __name__ == '__main__':
    sz50 = sz50()
    print(sz50)

    hs300 = hs300()
    print(hs300)

    zz500 = zz500()
    print(zz500)
