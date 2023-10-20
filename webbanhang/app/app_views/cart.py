from django.shortcuts import render
from app.app_views import user_authenticate


def cart(request):
    context_var = user_authenticate.user_authenticate(request)
    context = context_var
    return render(request, 'app/cart.html', context)
