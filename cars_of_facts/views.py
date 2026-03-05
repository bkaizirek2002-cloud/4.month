from django.http import HttpResponse

def car_fact_1(req):
    return HttpResponse("Факт №1 Первый автомобиль был создан в 1886 году.")

def car_fact_2(req):
    return HttpResponse("Факт №2 Самый быстрый автолмобиль в мире - Bugatti")

def car_fact_3(req):
    return HttpResponse("Фак №3 В мире более 1 миллиарда автомобилей.")
