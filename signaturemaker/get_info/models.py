from django.db import models

class UserInfo(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
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
    