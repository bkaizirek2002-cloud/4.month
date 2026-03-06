from  django.urls import path
from . import views

urlpatterns = [
    path('fact1/', views.car_fact_1, name='fact_1'),
    path('fact2/', views.car_fact_2, name='fact_2'),
    path('fact3/', views.car_fact_3, name='fact_3'),
]