from django.contrib import admin
from .models import Reservation

# register your models here.

class ReservationAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Reservation, ReservationAdmin)