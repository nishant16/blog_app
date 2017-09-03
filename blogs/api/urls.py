from django.conf.urls import url

from .views import BlogListAPIView


urlpatterns=[
    url(r'^list/', BlogListAPIView.as_view(), name='listview'), #ex:/
    # url(r'^post/(?P<id>\d+)/', views.view_post, name='n1'),	
    ]
