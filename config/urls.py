"""cozy_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.apps import apps


'''
from . import views
from .views import CustomObtainAuthToken
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth import views as auth_views
'''

forum_name = apps.get_app_config('forum').verbose_name
store_name = apps.get_app_config('store').verbose_name
accounts_name = apps.get_app_config('accounts').verbose_name
stream_name = apps.get_app_config('stream').verbose_name

from apps.forum import views as forum_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(('apps.forum.urls', forum_name), namespace='forum')),
    url(r'^', include(('apps.stream.urls', store_name), namespace='stream')),
    url(r'^', include(('apps.store.urls', store_name), namespace='store')),
    url(r'^', include(('apps.accounts.urls', accounts_name), namespace='accounts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
'''