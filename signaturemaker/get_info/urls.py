from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<first_name>/'
         '<last_name>/',
         views.get_user_info,
         name='user info'
         ),
    path('<int:identifier>/',
         views.get_user_info,
         name='user info2'
         )
    
]