from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('massagecenterapp.urls')),
    path('services/', include('services.urls')),

]
