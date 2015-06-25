from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import blog_text

def parse_created_time(time):
    return time[ : 7]

        
#def add_time_category(blog_text):
#    blog_text.time_category = parse_created_time(str(blog_text.b_created_time))
#    blog_text.save()

def show_front(request):
    year = ['2015']
    
    _blog_ordered_by_time = blog_text.objects.order_by('-b_created_time')
    if _blog_ordered_by_time: 
        _oldest_year = int(str(_blog_ordered_by_time.reverse()[0].b_created_time)[ : 4])
        _latest_year = int(str(_blog_ordered_by_time[0].b_created_time)[ : 4])
        for i in range(_oldest_year, _latest_year + 1):
            if str(i) not in year: 
                year.append(i) 
    _blog_front           = {'blog_data'     : _blog_ordered_by_time,
                             'time_category' : year 
                            }
    
    return render(request, 'lovehome/front_page.html', _blog_front)

def show_time_category(request, year):
    year_array = ['2015'] 
    
    _blog_data                 = blog_text.objects.order_by('-b_created_time') 
    _oldest_year = int(str(_blog_data.reverse()[0].b_created_time)[ : 4])
    _latest_year = int(str(_blog_data[0].b_created_time)[ : 4])
    for i in range(_oldest_year, _latest_year + 1):
        if str(i) not in year_array: 
            year_array.append(i) 

    _blog_order_by_time   = _blog_data.filter(b_created_time__year = str(year))    
    _blog_year = {'blog_year'     : _blog_order_by_time, 
                  'blog_data'     : _blog_data, 
                  'time_category' : year_array
                 } 
    
    return render(request, 'lovehome/time_category.html', _blog_year)

def add_blog(request):
    if request.method == 'POST':
        
        #******************************************************************* 
        #if (blog_category.objects.filter(b_category = 'Jun')):
        #    _blog_category = blog_category.objects.get(b_category = 'Jun') 
        #else:
        #    _blog_category = blog_category(b_category = 'Jun')
        #    _blog_category.save()
        #******************************************************************* 
        
        _blog_text = blog_text(title        = request.POST['title'], 
                               blog_content = request.POST['blog'],
                               )
        _blog_text.save()
         
        return HttpResponseRedirect(reverse('lovehome:front_page'))
    else:
        return render(request, 'lovehome/add_blog.html')

def edit_blog(request, page_id):
    if request.method == 'POST':
        _blog_text              = blog_text.objects.get(pk=page_id)
        _blog_text.title        = request.POST['title']
        _blog_text.blog_content = request.POST['blog']
        _blog_text.save()
        return HttpResponseRedirect(reverse('lovehome:front_page'))
    else:
        _blog_data = blog_text.objects.get(pk=page_id)
        return render(request, 'lovehome/edit_blog.html', {'blog_data' : _blog_data})


def show_blog(request, page_id):
    _blog_data = get_object_or_404(blog_text, pk=page_id)
    return render(request, 'lovehome/show_blog.html', {'blog_data' : _blog_data})

def delete_blog(request, page_id):
    get_object_or_404(blog_text, pk=page_id).delete()
     
    return HttpResponseRedirect(reverse('lovehome:front_page'))
    










