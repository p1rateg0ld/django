from django import forms

# https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python
# Need to create a dictionary that can be imported, with specified allowed keys, so that the forms can be automatically imported 
# and the forms fields can be generated based on that dictionary

class NewUserForm(forms.Form):
    field_len = 50
    
    first_name    = forms.CharField(max_length= field_len)
    last_name     = forms.CharField(max_length= field_len)
    title         = forms.CharField(max_length= field_len)
    email_address = forms.CharField(max_length= field_len)
    work_phone    = forms.CharField(max_length= field_len)
    direct        = forms.CharField(max_length= field_len)
    department    = forms.CharField(max_length= field_len)
    # URL to a custom signature image
    link_address  = forms.CharField(max_length= field_len)
    # URL that the image should redirect to
    website_link  = forms.CharField(max_length= field_len)

