from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def home(request):
    context_var = user_authenticate.user_authenticate(request)
    products = Product.objects.all()
    vegetables = Product.objects.all().filter(category__slug="vegetable")
    fruits = Product.objects.all().filter(category__slug="fruits")
    herb = Product.objects.all().filter(category__slug="herb")
    context_var.update({'products': products, 'vegetables': vegetables, 'fruits': fruits, 'herb': herb})
    return render(request, 'app/home.html', context=context_var)
