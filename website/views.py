from django.shortcuts import render
from .models import Service

# Create your views here.
def home(request):
    service = Service.objects.all()
    return render(request, 'home.html', {'service': service})



# def privacy(request):
#     return render(request, 'privacy-policy.html', {})