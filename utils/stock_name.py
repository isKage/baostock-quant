import baostock as bs


def stock_name(code):
    # 登陆系统
    # bs.login()

    # 获取证券基本资料
    rs = bs.query_stock_basic(code=code)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

    # 登出系统
    # bs.logout()

    return data_list[0][1]

def stock_code(name):
    # 登陆系统
    # bs.login()

    # 获取证券基本资料
    rs = bs.query_stock_basic(code_name=name)

    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

    # 登出系统
    # bs.logout()

    return data_list[0][0]
