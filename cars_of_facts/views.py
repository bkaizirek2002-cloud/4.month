from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 
from .models import Car

def car_list(req):
    search_query = req.GET.get('search', '')
    if search_query:
        cars_list = Car.objects.filter(title__icontains=search_query) 
    else:
        cars_list = Car.objects.all()

    paginator = Paginator(cars_list, 3)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, 'car_list.html', {'page_obj': page_obj})

def car_detail_view(req, id):
    car = get_object_or_404(Car, id=id)
    car.views_count = 1  
    car.save()
    return render(req, 'car_detail.html', {'car': car})