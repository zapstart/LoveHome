from django.conf.urls import url

from .import views 

urlpatterns = [
    url(r'^$',                           views.show_front, name = 'front_page'),
    url(r'^add/$',                       views.add_blog,   name = 'add_blog'),
    url(r'^edit/(?P<page_id>\w+)/$',     views.edit_blog,  name = 'edit_blog'),
    url(r'^page/(?P<page_id>\w+)/$',     views.show_blog,  name = 'blog_page'),
]
