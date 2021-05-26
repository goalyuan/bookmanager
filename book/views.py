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
    return JsonResponse(data, status=400)

    #####################跳转页面#####################
    # return redirect('http://www.baidu.com')
    # 需求是跳转到首页
    # 通过reverse这个名字找到路径
    # path = reverse('book:index')
    # return redirect(path)

    return HttpResponse(data, status=400)


# 状态保持
# http://127.0.0.1:8000/set_cookie?username=admin
def set_cookie(request):
    """
    保存在客户端的数据cookie
    cookie是基于域名（ip）的
    0.概念
    1.流程（原理）
        第一次请求过程
        1.浏览器第一次请求服务器的时候，不会携带任何cookie信息
        2.服务器接收到请求之后，发现请求中没有任何cookie信息
        3.服务器设置一个cookie，这个cookie设置在响应中
        4.浏览器接收到这个响应后，发现响应中有cookie信息，浏览器会将cookie信息保存起来

        第二次及其之后的过程
        5.浏览器第二次请求及其之后的请求都会携带cookie信息
        6.我们的服务器接收到请求之后，会发现请求中携带的cookie信息，这样的话就认识是谁的请求了
    2.看效果
    3.从http协议角度深入掌握cookie的流程（原理）
        第一次
            1.第一次请求服务器，不会携带任何cookie信息，请求头中没有任何cookie信息
            2.服务器会为响应设置cookie信息，响应头中有set_cookie信息
        第二次及其之后
            3.第二次及其之后的请求都会携带cookie信息，请求头中有cookie信息
            4.（可选）在当前我们的代码中，没有在响应头中设置cookie，所以响应头中没有set_cookie信息

保存在服务器的数据叫session
session需要依赖于cookie
如果浏览器禁用了cookie，则session不能实现
    0.概念
    1.流程
        第一次请求：
            1.第一次请求携带一些（用户名/密码)，cookie没有任何信息
            2.服务器接收
    2.效果
    3.从原理（http）角度


    """
    # 第一次请求
    # 1.先判断有没有cookie
    # request.COOKIES
    # 2.获取用户名
    username = request.GET.get('username')
    # 3.因为我们没有假设没有cookie信息，我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')
    response.set_cookie('username', username, max_age=3600)
    # 4.返回响应
    # 删除cookie方式
    # response.delete_cookie(key='username')
    # response.set_cookie(key='username',value='admin',max_age=0)

    return response


# http://127.0.0.1:8000/get_cookie
def get_cookie(request):
    """
    第二次及其之后的过程
        5.浏览器第二次请求及其之后的请求都会携带cookie信息
        6.我们的服务器接收到请求之后，会发现请求中携带的cookie信息，这样的话就认识是谁的请求了
    """
    # 1.服务器可以接收（查看）cookie信息
    cookies = request.COOKIES
    # cookies就是一个字典
    username = cookies.get('username')
    return HttpResponse(username)


# http://127.0.0.1:8000/set_session?username=admin&password=123
def set_session(request):
    """
    保存在服务器的数据叫session
    session需要依赖于cookie
    如果浏览器禁用了cookie，则session不能实现
        0.概念
        1.流程
            第一次请求：
                1.第一次请求携带一些（用户名/密码)，cookie没有任何信息
                2.服务器接收这个请求之后，进行用户名和密码的验证，验证没有问题可以设置session信息
                3.在设置session信息的同时（session信息保存在服务端），服务器会在响应头设置一个sessionid的cookie信息(由服务器自己设置的)
                4.客户端（浏览器）在接收到响应之后，会将cookie信息保存起来（保存sessionid的信息）
            第二次及其之后的请求：
                5.第二次及其之后的请求都会携带sessionid信息
                6.当服务器接收到这个请求之后，会获取到sessionid信息，然后进行验证，验证成功则获取sessionid信息
        2.效果
            第一次请求：
                1.
        3.从原理（http）角度
    """
    # 1.
    print(request.COOKIES)
    # 2.对用户名和密码进行验证
    # 假设认为用户名和密码正确
    user_id = 6666
    # 3.设置session信息
    request.session['user_id'] = user_id
    # 4.返回响应
    return HttpResponse('set_session')


def get_session(request):
    """
    第二次及其之后的请求：
                5.第二次及其之后的请求都会携带sessionid信息
                6.当服务器接收到这个请求之后，会获取到sessionid信息，然后进行验证，验证成功则获取sessionid信息
    """
    # 1.请求都会携带sessionid信息
    print(request.COOKIES)
    # 2.会获取到sessionid信息，
    # 然后进行验证，验证成功则获取sessionid信息
    # request.session是字典
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')
    return HttpResponse('get_session')
