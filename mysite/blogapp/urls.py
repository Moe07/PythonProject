from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
     path("", views.blog_index, name="blog_index"),
     url(r'^add_post/$', views.add_post, name='add_post'),
     url(r'^add_post_form_submission/$', views.add_post_form_submission, name='add_post_form_submission'),
     path("<int:pk>/", views.blog_detail, name="blog_detail"),
]
