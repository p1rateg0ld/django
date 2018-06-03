from django.forms import ModelForm

from get_info.models import UserInfo

class NewUserForm(ModelForm):

    class Meta:
        model = UserInfo
        desired_variables_list = []
        
        model_variables = model.__dict__['__doc__']
        field_variables = model_variables[model_variables.index('(')+1:model_variables.rindex(')')].split(',')
        field_variables = [field_variable.strip() for field_variable in field_variables]
        for field_variable in field_variables:
            if field_variable != "pub_date" and field_variable != "id":
                desired_variables_list.append(field_variable)   

        fields = desired_variables_list
    
    
        
"""
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__()
        field_len = 50
        try:
            for field_name in kwargs['model_fields']:
                print(field_name)
                if field_name not in NewUserForm.__dict__.keys():
                    label = field_name.title().replace("_"," ")
                    #setattr(self,field_name,forms.CharField(max_length= field_len, label= label))
                    #locals()[field_name]=forms.CharField(max_length= field_len, label= label)
                    self.fields[field_name]=forms.CharField(max_length= field_len, label= label)
                   
        except KeyError:
            print("KeyError")
            self = NewUserForm(model_fields=[])
        

    def get_desired_attr(self):
        for name,value in self.cleaned_data.items():
            yield (self.__dict__[name].label, value)
"""

