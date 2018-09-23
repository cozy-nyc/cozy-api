from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<user__username>[\w\-]+)/$', views.ProfileDetail.as_view()),
    url(r'^profile/edit/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view()),
    url(r'^register', views.UserCreate.as_view(), name = 'account-create')
]
