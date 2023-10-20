from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def search_item(request):
    context_var = user_authenticate.user_authenticate(request)
    if request.method == "POST":
        searched = request.POST['searched']
        keys = Product.objects.filter(name__icontains=searched)
        numbers = keys.count()
        context = {'searched': searched, 'keys': keys, 'cart_items': context_var['cart_items'],
                   "context_var": context_var, 'numbers': numbers}
    else:
        context = {'searched': "", 'keys': "", 'cart_items': context_var['cart_items'], "context_var": context_var,
                   'numbers': 0}
    return render(request, 'app/search.html', context=context)
