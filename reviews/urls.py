from django.conf.urls import url
from django.contrib import admin
from reviews import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_product', views.add_product, name='add_product'),
    url(r'^details/(?P<product_slug>[\w\-]+)/$', views.product_detail, name='product_detail'),
    url(r'^search', views.search_product, name='search'),
    url(r'^add_comment/(?P<product_slug>[\w\-]+)/(?P<user_id>[\w\-]+)/$', views.add_comment, name='add_comment'),
    url(r'^was_added', views.was_added, name='was_added'),
    url(r'^back_comment/(?P<comment_id>[\w\-]+)/(?P<username>[\w\-]+)/$', views.back_comment, name='back_comment'),
    url(r'^thumbs_up/(?P<product_slug>[\w\-]+)/(?P<username>[\w\-]+)/$', views.thumbsUp, name='thumbsUp'),
    url(r'^thumbs_down/(?P<product_slug>[\w\-]+)/(?P<username>[\w\-]+)/$', views.thumbsDown, name='thumbsDown'),
    url(r'^profile_view/(?P<username>[\w\-]+)/$', views.profile_view, name='profile_view'),
    url(r'^view_user/(?P<username>[\w\-]+)/$', views.view_user, name='view_user'),
    url(r'^messenger/(?P<sender>[\w\-]+)/(?P<reciever>[\w\-]+)/(?P<body>[\a-z\d\-]+)/$', views.messenger, name='messenger'),
    url(r'^signin/$', views.signin),
    url(r'^signup/$', views.signup ),
    url(r'^signout/$', auth_views.logout, {'template_name': 'reviews/index.html'}),
    url(r'^check_message/(?P<username>[\w\-]+)/$', views.messagify, name='messagify'),
]
