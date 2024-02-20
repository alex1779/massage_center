from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.http import Http404

def reservations(request):
    context ={}
 
    # create object of form
    form = ReservationForm(request.POST or None)
    
    if form.is_valid():

        if Reservation.objects.all():

            for reservation in Reservation.objects.all():
                
                if form.instance.name == reservation.name and form.instance.service == reservation.service and form.instance.date == reservation.date and form.instance.hour == reservation.hour:
                    print("Ya existe. no se guarda.")
                    return render(request, "duplicate/duplicate.html")
                

            form.save()
            context['form']= form
            return render(request, "reservate/reservate.html", context)


        else:

            print("Se guarda. es la primera reserva")
            form.save()
            context['form']= form
            return render(request, "reservate/reservate.html", context)

                



 
    context['form']= form
    return render(request, "reservations/reservations.html", context)