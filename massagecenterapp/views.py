from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):

    return render(request, "massagecenterapp/home.html")


def AboutUs(request):

    return render(request, "massagecenterapp/about.html")


def qualityAssurance(request):

    return render(request, "massagecenterapp/quality.html")


def reservations(request):

    return render(request, "massagecenterapp/reservations.html")


def contact(request):

    return render(request, "massagecenterapp/contact.html")