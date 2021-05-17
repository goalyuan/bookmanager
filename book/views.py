from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
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
    # 1/100
    print(book_id, category_id)
    return HttpResponse('detail')
