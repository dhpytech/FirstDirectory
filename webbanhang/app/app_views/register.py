from django.shortcuts import render, redirect
from app.models import *
from app.app_views import user_authenticate


def register(request):
    context_var = user_authenticate.user_authenticate(request)
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page', permanent=True)
    context_var.update({'form': form})
    return render(request, 'app/register.html', context=context_var)
