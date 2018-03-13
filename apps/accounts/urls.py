from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
    url(r'^profile/edit/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view())
]