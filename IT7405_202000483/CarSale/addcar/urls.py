from django.urls import path
from . import views

app_name='addcar'
urlpatterns = [
    path('', views.addItem, name='addcar'),
]
