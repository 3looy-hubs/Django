from django.urls import path
from carview import views

app_name='carview'
urlpatterns =[
    path('',views.car_list,name="homePage"),
    path('searchcars',views.searchcars,name="searchcars"),
]