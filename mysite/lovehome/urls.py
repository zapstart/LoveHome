from django.conf.urls import url

from .import views 

urlpatterns = [
    url(r'^front/$',                 views.show_front, name = 'front_page'),
    url(r'^edit/$',                  views.add_blog,   name = 'edit_blog'),
    url(r'^page/(?P<page_id>\w+)/$', views.show_blog,  name = 'blog_page'),
]
