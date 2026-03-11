from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('myShop.urls')),
    path('cars/', include('cars_of_facts.urls')),
]