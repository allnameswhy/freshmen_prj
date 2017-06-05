"""archive_maker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    url(r'^createtable/$', views.TableCreateView.as_view(), name = 'create-table'),
    url(r'^mytables/$', views.TableListView.as_view(), name = 'list-table'), #immediately after login
    url(r'^mytables/(?P<table_no>[0-9]+)/$', views.TableDetailView.as_view(), name = 'detail-table'),
    url(r'^mytables/?P<table_no>[0-9]+/delete/$', views.TableDeleteView.as_view(), name = 'delete-table'), # unseen from the user
    url(r'^updatetable/?P<table_no>[0-9]+/$', views.TableUpdateView.as_view(), name = 'update-table')
  #  url(r'^mytables/?P<table_no>[0-9]+/item/?P<item_no>[0-9]+/$', views.ItemDetailView.as_view(), name = 'detail-item'), # from detail view of the table
  #  url(r'^updatetalbe/?P<table_no>[0-9]+/createitem/$', views.ItemCreateView.as_view(), name = 'create-item'),
  #  url(r'^updatetable/?P<table_no>[0-9]+/deleteitem/?P<item_no>[0-9]+/$', views.ItemDeleteView.as_view(), name = 'delete-item'), # unseen from the user
  #  url(r'^updatetable/?P<table_no>[0-9]+/updateitem/?P<item_no>[0-9]+/$', views.ItemUpdateView.as_view(), name = 'update-item'), # from update view of the table
]
