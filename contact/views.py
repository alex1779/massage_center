from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import EmailMessage

def contact(request):

    contact_form=contactForm()


    if request.method=="POST":
        contact_form=contactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")

            email=EmailMessage("Mensaje desde App Django",
               "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(name,email,content),
               "pruebastest577@gmail.com",["alex1779@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")



    return render(request, "contact/contact.html", {'myForm':contact_form})