from django.conf.urls import url

from pay.views import order

urlpatterns = [
    url(r'^order/$', order),
]
