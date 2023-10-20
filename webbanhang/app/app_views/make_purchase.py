from django.shortcuts import render
from app.models import *
from app.app_views import user_authenticate


def make_purchase(request):
    customer = request.user
    context_var = user_authenticate.user_authenticate(request)
    order = context_var['order']
    if request.method == "POST":
        invoice = Invoice.objects.create(customer=customer)
        items_checked = request.POST.getlist('checked')
        for i in items_checked:
            item = order.orderitems_set.get(pk=i)
            invoice_item = InvoiceItems.objects.create(invoice=invoice, product=item.product, quantity=item.quantity)
            invoice_item.save()
            order_item = OrderItems.objects.get(product=item.product)
            order_item.delete()
    else:
        pass
    invoice_current = Invoice.objects.all().filter(invoice_status='Not Finished').order_by('-date_status')[0]
    items_checked_list = invoice_current.invoiceitems_set.all()
    context_var.update({'items_checked_list': items_checked_list, 'invoice_current': invoice_current})
    return render(request, 'app/checkout.html', context=context_var)
