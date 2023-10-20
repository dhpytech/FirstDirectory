from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def category_item(request):
    context_var = user_authenticate.user_authenticate(request)
    active_category = request.GET.get('category', '')
    products = Product.objects.filter(category__slug=active_category)
    context_var.update({'products': products, 'active_category': active_category})
    return render(request, 'app/category.html', context=context_var)
