"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

"""
1.urlpatterns固定写法，值为列表
2.浏览器中输入的路径和urlpatterns中每一项顺序进行匹配
3.urlpatterns中元素为url
url的第一个参数是正则，r是转义，^是开始，$是严格的结尾
4.浏览器中的路由http://ip:port/path/?key=value,http://ip:port/不参与匹配
5.如果和当前某一项匹配成功，则引导到子应用中继续匹配
如果匹配成功，则停止匹配返回响应的视图
如果匹配不成功，则继续和后面的工程中的url的每一项继续匹配，直到匹配每一项
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='home'),

    # 添加一项
    # 只要不是admin/肯定会走这个
    # 如果设置了namespace这个时候需要通过namespace:name来获取路由
    # path=reversed('book:index')
    # print(path)
    url(r'^', include('book.urls', namespace='book'), ),
    url(r'^pay/', include('pay.urls')),
]
