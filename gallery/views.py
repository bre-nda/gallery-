from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Location

# Create your views here.
def welcome(request):
    category = Category.objects.all()
    location = Location.objects.all()

    return render(request, 'index.html', {"location": location,"category":category})


