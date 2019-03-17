# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test(name='django')  # 相当于SQL中的INSERT
    test1.save()
    # response = ""  # 初始化
    # list = Test.objects.all()  # 相当于SQL中的SELECT * FROM
    # # response2 = Test.objects.filter(id=1)  # filter相当于SQL中的WHERE
    # # response3 = Test.objects.get(id=1)  # 获取单个对象
    # Test.objects.order_by('name')[0:2]  # 限制返回的数据，相当于 SQL 中的 OFFSET 0 LIMIT 2
    # Test.objects.order_by("id")  # 数据排序
    # Test.objects.filter(name="django").order_by("id")  # 可以连锁使用
    # Test.objects.filter(id=1).update(name='Google')  # 修改数据可以使用 save() 或 update()
    # Test.objects.filter(id=3).delete()  # 删除数据库中的对象只需调用该对象的delete()方法
    # # 输出所有数据
    # for var in list:
    #     response += var.name + " "
    # return HttpResponse("<p>" + response + "</p>")
    return HttpResponse("<p>数据添加成功！</p>")
