from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^menu/create/$', views.menu_create, name='menu_create'),
    url(r'^menu/save/new/$', views.post_menu_create, name='post_menu_create'),
    url(r'^menu/(?P<menu_id>[a-zA-Z0-9]+)/$', views.change_form, name='change_form'),
    url(r'^item/(?P<menu_id>[a-zA-Z0-9]+)/$', views.item_form, name='item_form'),
    url(r'^menu/delete/(?P<menu_id>[0-9]+)/$', views.menu_delete, name='menu_delete'),
    url(r'^item/delete/(?P<item_id>[0-9]+)/$', views.item_delete, name='item_delete'),
    url(r'^menu/save$', views.post_change_form, name='post_change_form'),
    url(r'^menu/$', views.menu_list, name='menu'),
    url(r'^item/$', views.item_list, name='list'),
]