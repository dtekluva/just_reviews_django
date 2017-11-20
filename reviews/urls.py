from django.conf.urls import url
from django.contrib import admin
from reviews import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product_detail', views.product_detail, name='product_detail'),
    url(r'^details/(?P<product_slug>[\w\-]+)/$', views.product_detail, name='product_detail'),
    url(r'^search', views.search_product, name='search'),
    url(r'^add_comment/(?P<product_slug>[\w\-]+)/$', views.add_comment, name='add_comment'),
    url(r'^was_added', views.was_added, name='was_added'),
    url(r'^back_comment/(?P<comment_id>[\w\-]+)/(?P<username>[\w\-]+)/$', views.back_comment, name='back_comment'),
    url(r'^thumbs_up/(?P<product_slug>[\w\-]+)/(?P<username>[\w\-]+)/$', views.thumbsUp, name='thumbsUp'),
    url(r'^thumbs_down/(?P<product_slug>[\w\-]+)/(?P<username>[\w\-]+)/$', views.thumbsDown, name='thumbsDown'),
    url(r'^signin/$', auth_views.login),
    url(r'^signup/$', views.signup ),
    url(r'^signout/$', auth_views.logout, {'template_name': 'reviews/index.html'}),
]
