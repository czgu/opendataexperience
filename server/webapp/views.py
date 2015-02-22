from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'webapp/index.html')

def tracker(request):
    return render(request, 'webapp/nutrition-tracker.html')

def about(request, item):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')
