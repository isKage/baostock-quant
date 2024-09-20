from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from utils.stock_index import code_index


def index(request):
    """ 首页 """
    return render(request, "index.html")


def sh_index(request):
    """ 上证指数 折线图 """

    # 上证指数 当前至6个月前
    sh_index = code_index(code='sh.000001', num_month=6)

    legend = ['上证指数']
    series_list = [
        {
            "name": '上证指数',
            "type": 'line',
            "data": sh_index['close'].to_list()
        }
    ]
    x_axis = sh_index['date'].to_list()

    # 返还给前台要序列化（针对Ajax）
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "x_axis": x_axis,
            "series_list": series_list,
        }
    }

    return JsonResponse(result)


def sz_index(request):
    """ 深证指数 折线图 """
    # 深证指数 当前至6个月前
    sz_index = code_index(code='sz.399106', num_month=5)

    legend = ['深证指数']
    series_list = [
        {
            "name": '深证指数',
            "type": 'line',
            "data": sz_index['close'].to_list()
        }
    ]
    x_axis = sz_index['date'].to_list()

    # 返还给前台要序列化（针对Ajax）
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "x_axis": x_axis,
            "series_list": series_list,
        }
    }

    return JsonResponse(result)
