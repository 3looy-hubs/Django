from django.shortcuts import render
from carview.models import Car

# Create your views here.

def car_list(request):
    car_objects = Car.objects.all()

    return render(request, 'carview/carview.html', {"car_objects": car_objects})

def searchcars(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        cars = Car.objects.filter(model__contains=searched)
        return render(request, 'carview/searchcars.html', {'searched': searched, 'cars': cars})
    else:
        return render(request, 'carview/searchcars.html', {})