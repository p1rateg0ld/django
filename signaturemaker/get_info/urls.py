from django.urls import path

from . import views

app_name = 'get_info'
urlpatterns = [
    path('', 
         views.IndexView.as_view(), 
         name='index'
         ),
    path('<first_name>/'
         '<last_name>/',
         views.DetailView.as_view(),
         name='detail'
         ),
    path('<int:pk>/', 
         views.DetailView.as_view(), 
         name='detail'
         ),
    path('new_user_form/', 
         views.new_user_form, 
         name='new_user'),
    path('signature_download/',
         views.signature_download,
         name='signature_download')
]