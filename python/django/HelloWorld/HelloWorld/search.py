# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    content = request.GET['q']
    if content != '':
        message = '你搜索的内容为: ' + content
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
