from django.shortcuts import render, redirect


def reservations(request):


    if request.method=="POST":

        return redirect("/reservations/?novalido")


    return render(request, "reservations/reservations.html")