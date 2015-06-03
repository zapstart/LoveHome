from django.db import models

class blog_text(models.Model):
    title          = models.CharField(max_length = 50) 
    b_created_time = models.TimeField(auto_now_add = True, blank = True)
    b_update_time  = models.TimeField(auto_now = True, blank = True)
    blog_content   = models.TextField(blank = True)
    
