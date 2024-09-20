from django.urls import path
from app01.views import index, individual

urlpatterns = [
    # 首页
    path("index/", index.index, name="index"),
    path("index/sh_index/", index.sh_index, name="sh_index"),
    path("index/sz_index/", index.sz_index, name="sz_index"),

    # 个股
    path("individual/", individual.individual, name="individual"),
]
