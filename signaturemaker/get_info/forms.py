from django import forms
from get_info.models import UserInfo




# https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python
# Need to create a dictionary that can be imported, with specified allowed keys, so that the models can be automatically imported 
# and the form fields can be generated based on that dictionary

class UserInfoForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)