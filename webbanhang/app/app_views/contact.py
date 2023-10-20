from django.contrib import messages

from app.app_views import user_authenticate
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail, mail_admins, BadHeaderError


def contact_us(request):
    context_var = user_authenticate.user_authenticate(request)
    return render(request, 'app/contact.html', context=context_var)


def contact_information(request):
    if request.method == 'POST':
        # Feedback of client
        client_name = request.POST.get('name')
        client_phone = request.POST.get('phone')
        client_email = request.POST.get('email')
        client_content = request.POST.get('content')

        # Info to client
        subject_to_client = 'Thank you for your feedback'
        message_to_client = f'Hi {client_name}! Thank you for feedback. We will reply to you as soon as possible'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [client_email]

        # Info to admin
        subject_to_admin = f'We have one feedback'
        content_of_feedback = f'From {client_name}\nEmail: {client_email}\nPhone: {client_phone}\n' \
                              f'Content: {client_content}'

        # Send Email
        if client_name and client_email and client_content:
            try:
                mail_admins(subject_to_admin, content_of_feedback, fail_silently=False)
                send_mail(subject_to_client, message_to_client, email_from, recipient_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid Header Found.")
            messages.success(request, 'thank you for your feedback! We will response to you as soon as possible.')
            return redirect('contact', permanent=True)
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
    else:
        return HttpResponse("Something is wrong - Find and Fix it")
