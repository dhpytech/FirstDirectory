from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def about_us(requests):
    member_team = TeamMember.objects.all()
    context_var = user_authenticate.user_authenticate(requests)
    context_var.update({'member_team': member_team})
    return render(requests, 'app/about us.html', context=context_var)
