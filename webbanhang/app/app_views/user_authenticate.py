from app.models import *


def user_authenticate(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
        cart_items = order.get_cart_items
        user_detail = UserMoreDetails.objects.get(customer=customer)
        user_main_info = ShippingAddress.objects.get(customer=customer)
    else:
        items = []
        order = {'get_items': "", 'get_total': ""}
        cart_items = 0
        customer = ""
        user_detail = ""
        user_main_info = ""
    categories = Category.objects.filter(is_sub=False)
    return dict({'items': items, 'cart_items': cart_items, 'order': order, 'customer': customer,
                 'categories': categories, 'user_detail': user_detail, 'user_main_info': user_main_info})
