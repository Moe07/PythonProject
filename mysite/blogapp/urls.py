from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
     path("", views.blog_index, name="blog_index"),
     path("<int:pk>/", views.blog_detail, name="blog_detail"),
     url(r'^add_post_form_submission/$', views.add_post_form_submission, name='add_post_form_submission'),
     url(r'^edit_post_form_submission(?P<pk>\d+)/$', views.edit_post_form_submission, name='edit_post_form_submission'),
     url(r'^edit_post(?P<pk>\d+)/$', views.edit_post, name="edit_post"),
]
