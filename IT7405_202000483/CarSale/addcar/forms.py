from django import forms

class AddCar(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    brand = forms.CharField()
    model = forms.CharField()
    price = forms.FloatField()
    year = forms.IntegerField()
    kilometers = forms.CharField()
    transmission = forms.CharField()
    description = forms.CharField()
    image = forms.FileField()