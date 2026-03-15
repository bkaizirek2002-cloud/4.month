from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('myShop.urls')),
    path('cars/', include('cars_of_facts.urls')),
    path('tourism/', include('tourism.urls')),
    path('drivers/', include('drivers.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('captcha/', include('captcha.urls')),
]
