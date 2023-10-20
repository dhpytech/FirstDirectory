from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def detail(request):
    context_var = user_authenticate.user_authenticate(request)
    id_items = request.GET.get('id', '')
    product_detail = Product.objects.filter(id=id_items)
    context_var.update({'product_detail': product_detail})
    return render(request, 'app/detail.html', context=context_var)
