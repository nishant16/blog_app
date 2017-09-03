from django.conf.urls import url

from . import views


urlpatterns=[
    url(r'^$', views.index, name='index'), #ex:/
    url(r'^post/(?P<id>\d+)/', views.view_post, name='n1'),
    url(r'^category/(?P<id>\d+)/', views.view_category, name='n2'),
    url(r'^create/', views.create, name='n3'),
    url(r'^edit/$', views.edit, name='n4'),
    url(r'^edit/(?P<id>\d*)/', views.edit_blog_category, name='n5'),
    url(r'^blogform/$',views.create_form,name='n6'),
    url(r'^modelform/$',views.create_model_form,name='n7'),
    url(r'^login/',views.login, name ='n8'),
    url(r'^data/',views.data_list,name='n9'),

    ]

