from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register(request):
    context_var = user_authenticate(request)
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page', permanent=True)
    context_var.update({'form': form})
    return render(request, 'app/register.html', context=context_var)


def login_page(request):
    context_var = user_authenticate(request)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'User or Password is not correct!')
    return render(request, 'app/login.html', context=context_var)


def logout_page(request):
    logout(request)
    return redirect('home')


def user_authenticate(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
        cart_items = order.get_cart_items
        user_detail = UserMoreDetails.objects.get(customer=customer)
    else:
        items = []
        order = {'get_items': "", 'get_total': ""}
        cart_items = 0
        customer = ""
        user_detail = ""
    categories = Category.objects.filter(is_sub=False)
    return dict({'items': items, 'cart_items': cart_items, 'order': order, 'customer': customer,
                 'categories': categories, 'user_detail': user_detail})


def home(request):
    context_var = user_authenticate(request)
    products = Product.objects.all()
    vegetables = Product.objects.all().filter(category__slug="vegetable")
    fruits = Product.objects.all().filter(category__slug="fruits")
    herb = Product.objects.all().filter(category__slug="herb")
    context_var.update({'products': products, 'vegetables': vegetables, 'fruits': fruits, 'herb': herb})
    return render(request, 'app/home.html', context=context_var)


def category_item(request):
    context_var = user_authenticate(request)
    active_category = request.GET.get('category', '')
    products = Product.objects.filter(category__slug=active_category)
    context_var.update({'products': products, 'active_category': active_category})
    return render(request, 'app/category.html', context=context_var)


def search_item(request):
    context_var = user_authenticate(request)
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


def cart(request):
    context_var = user_authenticate(request)
    context = context_var
    return render(request, 'app/cart.html', context)


def checkout(request):
    context_var = user_authenticate(request)
    invoice_current = Invoice.objects.all().filter(invoice_status='Not Finished').order_by('-date_status')[0]
    items_checked_list = invoice_current.invoiceitems_set.all()
    context = {'items': context_var['items'], 'order': context_var['order'], 'cart_items': context_var['cart_items'],
               'customer': context_var['customer'], 'items_checked_list': items_checked_list,
               'invoice_current': invoice_current}
    return render(request, 'app/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItems.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse('added', safe=False)


def detail(request):
    context_var = user_authenticate(request)
    id_items = request.GET.get('id', '')
    product_detail = Product.objects.filter(id=id_items)
    context_var.update({'product_detail': product_detail})
    return render(request, 'app/detail.html', context=context_var)


def profile(request):
    invoice_list = Invoice.objects.all().filter(invoice_status='Not Finished').order_by('-date_status')[:5]
    invoice_list_template = []
    for invoice in invoice_list:
        invoice_detail = invoice.invoiceitems_set.all()
        invoice_status = invoice.invoice_status
        invoice_list_template.append([invoice_status, invoice_detail])
    context_var = user_authenticate(request)
    context_var.update({'invoice_list_template': invoice_list_template})
    return render(request, 'app/profile.html', context=context_var)


def make_purchase(request):
    customer = request.user
    context_var = user_authenticate(request)
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


def about_us(requests):
    member_team = TeamMember.objects.all()
    context = {'member_team': member_team}
    return render(requests, 'app/about us.html', context=context)


def contact_us(requests):
    context = {}
    return render(requests, 'app/contact.html', context=context)
