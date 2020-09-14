from django.shortcuts import render


# Create your views here.

def contact_main(request, path=None):
    return render(request, "contact_main.html", {})
