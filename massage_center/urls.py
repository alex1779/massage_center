from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('massagecenterapp.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('reservations/', include('reservations.urls')),
    path('authentication/', include('authentication.urls')),
]
