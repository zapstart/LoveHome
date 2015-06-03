from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import blog_text

def show_front(request):
    _blog_ordered_by_time = blog_text.objects.order_by('-b_created_time')
    _blog_data            = {'blog_data' : _blog_ordered_by_time} 
    return render(request, 'lovehome/front_page.html', _blog_data)

def add_blog(request):
    if request.method == 'POST':
        _blog_text = blog_text(title        = request.POST['title'], 
                               blog_content = request.POST['blog']) 
        _blog_text.save()
        return HttpResponseRedirect(reverse('lovehome:front_page'))
    else:
        return render(request, 'lovehome/edit_blog.html')

def show_blog(request, page_id):
    _page_id   = page_id
    _blog_data = blog_text.objects.get(pk=_page_id)
    return render(request, 'lovehome/show_blog.html', {'blog' : _blog_data})
      
    
