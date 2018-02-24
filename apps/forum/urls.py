from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^board/$', views.BoardList.as_view()),
    url(r'^board/(?P<pk>[0-9]+)/$', views.BoardDetail.as_view()),
    url(r'^board/create$', views.BoardCreate.as_view()),
    url(r'^thread/$', views.ThreadList.as_view()),
    url(r'^thread/create$', views.ThreadCreate.as_view()),
    url(r'^thread/(?P<pk>[0-9]+)/$', views.ThreadDetail.as_view()),
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/create$', views.PostCreate.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),

]
