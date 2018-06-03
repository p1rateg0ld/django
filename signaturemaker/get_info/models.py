from django.db import models
from django.utils import timezone

from itertools import chain
from datetime import timedelta





# https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python


class UserInfo(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    # return a dictionary of user info
    def get_user_details(self):    
        # return a dictionary of user info
        details = {}
        for key,value in vars(self).items():
            new_key = key.title()
            if type(value) == str:
                try:
                    new_key = new_key.replace("_", " ")
                except:
                    pass
                details[new_key] = value
        return details    
                    
        
    
    field_len = 50
    
    first_name    = models.CharField(max_length= field_len)
    last_name     = models.CharField(max_length= field_len)
    title         = models.CharField(max_length= field_len)
    email_address = models.CharField(max_length= field_len)
    work_phone    = models.CharField(max_length= field_len)
    direct        = models.CharField(max_length= field_len)
    department    = models.CharField(max_length= field_len)
    # URL to a custom signature image
    link_address  = models.CharField(max_length= field_len)
    # URL that the image should redirect to
    website_link  = models.CharField(max_length= field_len)
    pub_date      = models.DateTimeField('date published')
    