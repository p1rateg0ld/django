from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone

from datetime import datetime

from get_info.models import UserInfo
from get_info.forms import NewUserForm
from signature_maker import info, make_HTML
from get_info.templatetags.get_info_extras import user_vars

#### Helper Functions ####


def find_user(**kwargs):
    print("######################################")
    print(kwargs)
    try:
        return UserInfo.objects.filter(first_name= kwargs["first_name"], last_name= kwargs["last_name"])
    except KeyError:
        try:
            return UserInfo.objects.filter(id=kwargs["identifier"])
        except KeyError:
            return False


def create_new_user(data_object):
    new_user = UserInfo()
    new_user.pub_date = datetime.now()
    print(data_object)
    [setattr(new_user, key, value) for key,value in data_object.items()]
    new_user.save()
    return new_user
    
    
#### Views ####
        
class IndexView(generic.ListView):
    template_name = 'get_info/index.html'
    context_object_name = 'all_users'
    
    def get_queryset(self):
        #Return all users
        return UserInfo.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = UserInfo
    
    template_name = 'get_info/user_template.html' 
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = kwargs['object']
        context['user_details'] = context['user'].get_user_details()
        
        if kwargs['object'].pub_date > timezone.now():
            raise Http404("No User Found")
        else:
            return context
        
        
"""
def get_user_info(request, identifier= '',first_name= '', last_name= ''):
    try:
        if identifier:
            # Using pk here to test 404 throw
            #matched_users = [UserInfo.objects.get(pk=identifier)]
            matched_users = find_user (identifier=identifier)
        else:
            matched_users = find_user(first_name= first_name, last_name= last_name)
        context = { 'matched_users': matched_users, }
    except UserInfo.DoesNotExist:
        raise Http404("No User Found")
    
    return render(request, 'get_info/user_template.html', context)
"""
            
# Interface to create a new user object to and store in the database
def new_user_form(request):
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            new_id = create_new_user(form.cleaned_data).id
            return HttpResponseRedirect("/get_info/" + str(new_id) + "/")
        else:
            print("invalid")
            form = NewUserForm()
    else:
        form = NewUserForm()
    return render(request, 'get_info/new_user_template.html', {'form':form})
