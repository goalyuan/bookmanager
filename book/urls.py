from django.conf.urls import url
from book.views import index, detail

urlpatterns = [
    url(r'^home/$', index, name='index'),
    # 127.0.0.1:8000/1/100
    #url(r'(1)/(100)/', detail),
    #根据位置获取url参数
    # url(r'(\d+)/(\d+)/', detail),
    url(r'(?P<category_id>\d+)/(?P<book_id>\d+)', detail),
]
