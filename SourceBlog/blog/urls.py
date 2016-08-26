from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list , name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    url(r'^new/post/$', views.post_new, name='new'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_edit, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
]
