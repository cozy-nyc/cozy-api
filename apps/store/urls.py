from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('images', views.ItemImageViewset, 'images')


urlpatterns = [
    url(r'^exchange/info/$', views.ExchangeService.as_view()),
    url(r'^exchange/category/$', views.CategoryList.as_view()),
 	url(r'^exchange/category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^exchange/item/$', views.ItemList.as_view()),
    url(r'^exchange/item/create/$', views.ItemCreate.as_view()),
 	url(r'^exchange/item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^exchange/item/edit/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view()),
    url(r'^exchange/item/delete/(?P<pk>[0-9]+)/$', views.ItemDelete.as_view()),
    url(r'^exchange/transactions/$', views.TransactionList.as_view()),
    url(r'^exchange/transactions/create/$', views.TransactionCreate.as_view()),
 	url(r'^exchange/transactions/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^exchange/transactions/edit/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view()),
    url(r'^', include(router.urls)),



]
