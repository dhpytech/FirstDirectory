from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.


def logout_page(request):
    logout(request)
    return redirect('home')
