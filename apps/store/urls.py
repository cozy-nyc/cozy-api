from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^category/$', views.CategoryList.as_view()),
 	url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^subCategory/$', views.SubCategoryList.as_view()),
    url(r'^subCategory/create$', views.SubCategoryCreate.as_view()),
 	url(r'^subCategory/(?P<pk>[0-9]+)/$', views.SubCategoryDetial.as_view()),
    url(r'^item/$', views.ItemList.as_view()),
    url(r'^item/create/$', views.ItemCreate.as_view()),
 	url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^item/edit/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view()),
    url(r'^item/delete/(?P<pk>[0-9]+)/$', views.ItemDelete.as_view()),
    url(r'^transactions/$', views.TransactionList.as_view()),
    url(r'^transactions/create/$', views.TransactionCreate.as_view()),
 	url(r'^transactions/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^transactions/edit/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view()),

]
