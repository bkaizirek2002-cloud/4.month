from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('myShop.urls')),
=======
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars_of_facts.urls')),
>>>>>>> origin/main
]
