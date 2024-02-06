from django.urls import path
from massagecenterapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.Home, name="Home"),
    path('about/', views.AboutUs, name="About"),
    path('quality/', views.qualityAssurance, name="Quality"),
    path('reservations/', views.reservations, name="Reservations"),
    path('contact/', views.contact, name="Contact"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)