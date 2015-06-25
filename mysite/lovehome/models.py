from django.db import models

#class blog_category(models.Model):
#    b_category = models.CharField(max_length = 50, null = True, blank = True)  
#
#    def __str__(self):
#        return self.b_category 

class blog_text(models.Model):
    title          = models.CharField(max_length = 50, null = True, blank = True) 
    b_created_time = models.DateTimeField(auto_now_add = True, blank = True)
    b_update_time  = models.DateTimeField(auto_now = True, blank = True)
    blog_content   = models.TextField(null = True, blank = True)
#    time_category  = models.CharField(max_length = 50, null = True, blank = True)
    #category       = models.ForeignKey(blog_category, null = True, blank = True)
    
    def __str__(self):
        return str(self.title)

