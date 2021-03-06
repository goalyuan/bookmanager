from django.conf.urls import url
from book.views import index, detail, set_cookie, get_cookie, set_session, get_session, LoginView, HomeView

urlpatterns = [
    url(r'^home/$', index, name='home'),
    # 127.0.0.1:8000/1/100
    # url(r'(1)/(100)/', detail),
    # 根据位置获取url参数
    # url(r'(\d+)/(\d+)/', detail),
    # 关键字参数--推荐使用这种方式
    url(r'(?P<category_id>\d+)/(?P<book_id>\d+)', detail),
    # cookie第一次请求
    url(r'^set_cookie', set_cookie),
    # cookie第二次及其之后的请求
    url(r'^get_cookie', get_cookie),
    #
    url(r'^set_session', set_session),
    url(r'^get_session', get_session),

    # 类视图的路由
    # url的第一个参数是正则
    # url的第二个参数是视图函数名
    url(r'^login/$', LoginView.as_view()),
    url(r'^index/$', HomeView.as_view()),
]
