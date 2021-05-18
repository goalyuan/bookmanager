import json

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
from django.urls import reverse

from book.models import BookInfo

"""
视图
1.就是python函数
2.函数的第一个参数就是请求,和请求相关的，它是HTTPRequest的实例对象
3.函数必须返回一个响应，响应是HTTPResponse的实力对象或子类实例对象
"""


def index(request):
    """
    reversed就是通过name来动态获取路径（路由）
    如果没有设置namespace则可以通过name来获取reverse(name)
    如果有设置namespace则可以通过namespace:name来获取reverse(namespace:name)

    登录成功之后跳转到首页
    注册成功之后跳转到首页
    :param request:
    :return:
    """
    path = reversed('index')
    print(path)
    return HttpResponse("index")


#
# def index(request):
#     name = '小菊花'
#     # return HttpResponse('index')
#     # request,template_name,context=None
#     # 参数1 当前的请求
#     # 参数2 模板文件
#     # 参数3 传递参数
#     context = {
#         'name': name,
#     }
#     return render(request, 'index.html', context=context)


# def index(request):
#     # 1.到数据库中查询书籍
#     books = BookInfo.objects.all()
#     # 2.组织数据
#     context = {
#         'name': books,
#     }
#     # 3.传递给模板
#     render(request,)
#     return HttpResponse('index')


def detail(request, book_id, category_id):
    # 根据位置获取参数
    # 1/100
    # print(category_id, book_id)

    #####################GET 查询字符串#####################
    """
     https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%AD%97%E7%AC%A6%E4%B8%B2&fenlei=256&rsv_pq=9ab8f86f008e261f&rsv_t=21b2VkCOc2NGU71mMOfPRi0Fuw0U2OMadmzPODJYWx3fcPuvotBMFfz1bSk&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=13&rsv_sug1=30&rsv_sug7=100
     以？作为1个分隔
     ？前边表示路由
     ？后边表示get方式传递的参数，称之为 查询字符串
     ?key=value&key=value...
    """""
    # QueryDict和Dict区别，QueryDict一个键有可能多个值
    # params = request.GET
    # print(params)  # <QueryDict: {'username': ['admin', 'tom'], 'password': ['123', '123']}>
    # print(params['username'])  # QueryDict以普通字典方式获取一个键的值时，只能获取一个
    # print(params['password'])
    # usernames = params.getlist('username')  # QueryDict使用getlist方法获取多个值
    # password = params.get('password')  # QueryDict使用get方法获取1个值值
    # print(usernames)
    # print(password)

    #####################POST 表单#####################
    # data = request.POST
    # print(data)

    #####################POST Json数据#####################
    # print(request.POST)
    # print(request.body)  # b'{\r\n    "name":"tom",\r\n    "password":123456\r\n}'
    # print(type(request.body.decode()))  # 类型是str
    # body_str = request.body.decode()
    # """
    # json.dumps将字典转换为JSON形式的字符串
    # json.loads将JSON形式的字符串转为字典
    # """
    #
    # data = json.loads(body_str)
    # print(data)
    # print(data['name'])

    #####################请求头#####################
    # print(request.META)
    # print(request.META['CONTENT_TYPE'])
    # print(request.method)

    #####################响应HttpResponse#####################
    # data = {"name": "test"}
    # HttpResponse
    # content传递字符串不要传递对象、字典
    # status HTTP status code must be an integer from 100 to 599.只能使用系统规定的
    # content_type 是一个MIME类
    # 语法形式 大类/小类 text/html image/jpg
    #####################JsonHttpResponse#####################
    from django.http import JsonResponse
    data = {"name": "test"}
    return JsonResponse(data)

    #####################跳转页面#####################
    # return redirect('http://www.baidu.com')
    # 需求是跳转到首页
    # 通过reverse这个名字找到路径
    # path = reverse('book:index')
    # return redirect(path)

    return HttpResponse(data, status=400)
