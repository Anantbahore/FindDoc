from django.urls import path
from hostal_grievance.views import Home , Thanks , Submit ,data

app_name='hostal_grievance'
urlpatterns = [
    # path('' , Home.as_view() , name = 'HomePage'),
    path('home',data, name = 'homepage'),
    path('update',Submit.as_view() ,name ='data'), 
    path('success' , Thanks.as_view() , name = "success")
]
