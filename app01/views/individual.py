from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse

from utils.stock_index import stock_index
from utils.stock_name import stock_name

from datetime import datetime
import baostock as bs


def individual(request):
    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')
    stockname = '股票名称'

    if request.method == 'POST':
        code = request.POST.get('code', 'sz.399106')  # 获取股票代码
        date = request.POST.get('date', '')  # 获取开始日期

        # 查询股票名称
        stockname = stock_name(code)

        stock = stock_index(
            code=code,
            fields='date, close',
            start_date=date,
            end_date=current_date,
            frequency='d'
        )

        legend = [stockname]
        series_list = [
            {
                "name": stockname,
                "type": 'line',
                "data": stock['close'].to_list()
            }
        ]
        x_axis = stock['date'].to_list()

        # 返还给前台要序列化（针对Ajax）
        result = {
            "status": True,
            "data": {
                "title": stockname,
                "legend": legend,
                "x_axis": x_axis,
                "series_list": series_list,
            }
        }

        return JsonResponse(result)

    return render(request, "individual.html", {'name': stockname})


