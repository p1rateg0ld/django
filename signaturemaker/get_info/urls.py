from django.urls import path

from . import views

app_name = 'get_info'
urlpatterns = [
    path('', views.index, name='index'),
    path('<first_name>/'
         '<last_name>/',
         views.get_user_info,
         name='user_info'
         ),
    path('<int:identifier>/',
         views.get_user_info,
         name='id_lookup'
         ),
    path('new_user_form/', 
         views.new_user_form, 
         name='new_user')
    
]