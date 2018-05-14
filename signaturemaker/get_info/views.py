from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

from get_info.models import UserInfo
from get_info.forms import UserInfoForm

#### Helper Functions ####
def find_user(**kwargs):
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
    
    [setattr(new_user, key, value) for key,value in data_object.items()]
    new_user.save()
    return new_user  


#### Views ####
        
def index(request):
    
    all_users = UserInfo.objects.all()
    context = { 'all_users': all_users, }

    return render(request, 'get_info/index.html', context)

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


# Interface to create a new user object to and store in the database
def new_user_form(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            matched_users = find_user(first_name= form.cleaned_data["first_name"], last_name = form.cleaned_data["last_name"])
            if not matched_users:
                # create_new_user returns the UserInfo object, which has the id, which needs to be a string for the url
                return HttpResponseRedirect("/get_info/" + str((create_new_user(form.cleaned_data)).id) + "/")
            else:
                context = { 'matched_users': matched_users, }
                return render(request, 'get_info/user_template.html', context)
            
        
    else:
        form = UserInfoForm()
    return render(request, 'get_info/new_user_template.html', {'form':form})





    