from django.shortcuts import render,redirect
from carview.models import Car
from addcar.functions import handle_uploaded_file
from addcar.forms import AddCar
# Create your views here.
def addItem(request):
    if request.method == "POST":
        myForm = AddCar(request.POST, request.FILES)
        if myForm.is_valid():
            handle_uploaded_file(request.FILES['image']) ##image is the name of the filed that has the image file
            name = myForm.cleaned_data["name"]
            number = myForm.cleaned_data["number"]
            brand = myForm.cleaned_data["brand"]
            model = myForm.cleaned_data["model"]
            price = myForm.cleaned_data["price"]
            year = myForm.cleaned_data["year"]
            kilometers = myForm.cleaned_data["kilometers"]
            transmission = myForm.cleaned_data["transmission"]
            description = myForm.cleaned_data["description"]
            imageFileName = request.FILES['image'].name
            imagePath = "\carview\img\{0}".format(imageFileName) ## should be same as path you did in function
            galleryObj = Car(name=name,number=number,brand=brand,model=model,price=price,year=year,kilometers=kilometers,transmission = transmission,description=description,image=imagePath)
            galleryObj.save()
        
            
    else:
        myForm = AddCar()
    return render(request, "addcar/addcar.html", {"myForm": myForm})