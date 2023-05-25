from django.shortcuts import render
from .models import Product

def tovar_home(request):
    product = Product.objects.all()
    return render(request, 'tovar/tovar_home.html', {'product': product})
