<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
>>>>>>> 27dbb832712eec2d0416cb8d294dcf07ba93b67a
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('blog_app.urls')),
    path('', include('books.urls')),
    path('', include('orders.urls')),
    path('', include('user.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('shop/', include('myShop.urls')),
    path('cars/', include('cars_of_facts.urls')),
    path('tourism/', include('tourism.urls')),
    path('drivers/', include('drivers.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('captcha/', include('captcha.urls')),
]
>>>>>>> 27dbb832712eec2d0416cb8d294dcf07ba93b67a
