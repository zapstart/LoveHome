from django.conf.urls import url

from .import views 

urlpatterns = [
    url(r'^$',                           views.show_front, name = 'front_page'),
    url(r'^add/$',                       views.add_blog,   name = 'add_blog'),
    url(r'^edit/(?P<page_id>\d+)/$',     views.edit_blog,  name = 'edit_blog'),
    url(r'^page/(?P<page_id>\d+)/$',     views.show_blog,  name = 'blog_page'),
    url(r'^delete/(?P<page_id>\d+)/$',   views.delete_blog,  name = 'delete_blog'),
]
