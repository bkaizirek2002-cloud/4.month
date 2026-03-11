from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(req):
    cars = Car.objects.all()
    return render(req, 'car_list.html',{'cars': cars})

def car_detail_view(req, id):
    car = get_object_or_404(Car, id=id)
    return render(req, 'car_detail.html', {'car': car})

