from django.http import HttpResponse, Http404
from django.shortcuts import render

from get_info.models import UserInfo

def index(request):
    
    all_users = UserInfo.objects.all()
    context = { 'all_users': all_users, }

    return render(request, 'get_info/index.html', context)

def get_user_info(request, identifier= '',first_name='', last_name=''):
    try:
        if identifier:
            # Using pk here to test 404 throw
            matched_users = [UserInfo.objects.get(pk=identifier)]
            # matched_users = UserInfo.objects.filter(id=identifier)
        else:
            matched_users = UserInfo.objects.filter(first_name= first_name, last_name= last_name)
        context = { 'matched_users': matched_users, }
    except UserInfo.DoesNotExist:
        raise Http404("No User Found")
    
    return render(request, 'get_info/user_template.html', context)