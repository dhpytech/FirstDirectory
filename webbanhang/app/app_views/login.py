from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app.app_views import user_authenticate

# Create your views here.


def login_page(request):
    context_var = user_authenticate.user_authenticate(request)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        list_name = ['username', 'password']
        dict_data = {}
        for name in list_name:
            data = request.POST.get(name)
            dict_data.update({name: data})
        user = authenticate(request, username=dict_data['username'], password=dict_data['password'])
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'User or Password is not correct!')
    return render(request, 'app/login.html', context=context_var)
