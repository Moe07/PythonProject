from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
     path("", views.blog_index, name="blog_index"),
     path("<int:pk>/", views.blog_detail, name="blog_detail"),
     url(r'^add_post/$', views.add_post, name='add_post'),
     url(r'^edit_post(?P<pk>\d+)/$', views.edit_post, name="edit_post"),
     url(r'^delete_post(?P<pk>\d+)/$', views.delete_post, name="delete_post"),
]
