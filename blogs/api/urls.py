from django.conf.urls import url

from . import views


urlpatterns=[
    url(r'^list/', views.BlogListAPIView, name='listview'), #ex:/
    # url(r'^post/(?P<id>\d+)/', views.view_post, name='n1'),
    ]