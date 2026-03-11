from django.urls import path
from . import views 

urlpatterns = [
    path('', views.car_list, name='car_list'), 
    path('cars/<int:id>/', views.car_detail_view, name= 'car_detail'),
]