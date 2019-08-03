from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^info/$', views.ServiceList.as_view()),
]
