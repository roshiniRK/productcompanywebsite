from django.shortcuts import render


def company(request):
    return render (request,"home.html")

def products(request):
    return render(request,"products.html")

def people(request):
    return render(request,"people.html")

def contact(request):
    return render (request,"contact.html")