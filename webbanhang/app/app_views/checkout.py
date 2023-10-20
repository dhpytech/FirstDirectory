from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render, redirect
from app.models import *
from app.app_views import user_authenticate


def checkout(request):
    context_var = user_authenticate.user_authenticate(request)
    invoice_current = Invoice.objects.all().filter(invoice_status='Not Finished').order_by('-date_status')[0]
    items_checked_list = invoice_current.invoiceitems_set.all()

    user_address = context_var['user_main_info']
    user_detail = context_var['user_detail']
    user_infor_dict = {'Address': user_address.address, 'Country': user_address.country,
                       'City': user_address.city, 'Phone': user_detail.userPhone}

    context = {'items': context_var['items'], 'order': context_var['order'], 'cart_items': context_var['cart_items'],
               'customer': context_var['customer'], 'items_checked_list': items_checked_list,
               'invoice_current': invoice_current, 'user_infor_dict': user_infor_dict}
    if request.method == "POST":
        invoice_current.invoice_status = 'Wait for Confirmation'
        invoice_current.save()

        subject_to_admin = f'You have one Order on dhtech.pythonanywhere.com'
        report_order_to_admin = f'You have one oder from {request.user.username}\n' \
                                f'Email: {request.user.email}\nPhone: {user_detail.userPhone}'
        mail_admins(subject_to_admin, report_order_to_admin, fail_silently=False)
        messages.success(request, 'your order is ordered successfully. please check you address again. thank you!')
        return redirect('profile')
    return render(request, 'app/checkout.html', context)

