from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from app.models import Invoice, UserMoreDetails, ShippingAddress
from app.app_views import user_authenticate
from django.contrib.auth.models import User


def profile(request):
    invoice_list = Invoice.objects.all().order_by('-date_status')[:5]
    invoice_list_template = []
    for invoice in invoice_list:
        invoice_detail = invoice.invoiceitems_set.all()
        invoice_status = invoice.invoice_status
        invoice_list_template.append([invoice_status, invoice_detail])
    context_var = user_authenticate.user_authenticate(request)
    dict_name_type = {'first_name': 'text', 'last_name': 'text', 'email': 'email',
                      'address': 'text', 'city': 'text',
                      'userImage': 'file', 'userPhone': 'text', 'facebook': 'url', 'tiktok': 'url', 'twitter': 'url'}

    FileSystemStorage(location='/static/images')
    if request.method == "POST":
        current_user = User.objects.all().get(username=request.user)
        current_user.first_name = request.POST["first_name"] if request.POST["first_name"] != "" else current_user.first_name
        current_user.last_name = request.POST["last_name"] if request.POST["last_name"] != "" else current_user.last_name
        current_user.email = request.POST["email"] if request.POST["email"] != "" else current_user.email
        current_user.save()

        user_detail = UserMoreDetails.objects.get(customer=request.user)
        user_detail.userImage = request.FILES["userImage"] if request.FILES else user_detail.userImage
        user_detail.userPhone = request.POST["userPhone"] if request.POST["userPhone"] != "" else user_detail.userPhone
        user_detail.facebook = request.POST["facebook"] if request.POST["facebook"] != "" else user_detail.facebook
        user_detail.tiktok = request.POST["tiktok"] if request.POST["tiktok"] != "" else user_detail.tiktok
        user_detail.twitter = request.POST["twitter"] if request.POST["twitter"] != "" else user_detail.twitter
        user_detail.save()

        user_address = ShippingAddress.objects.get(customer=request.user)
        user_address.address = request.POST["address"] if request.POST["address"] != "" else user_address.address
        user_address.city = request.POST["city"] if request.POST["address"] != "" else user_address.address

        messages.success(request, 'your profile is updated! ')
        return redirect('profile', permanent=True)

    context_var.update({'invoice_list_template': invoice_list_template, 'dict_name_type': dict_name_type})
    return render(request, 'app/profile.html', context=context_var, )
