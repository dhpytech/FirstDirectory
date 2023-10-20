from django.urls import path
from .app_views import contact, register, home, login, logout, category_item, search_item, cart
from .app_views import make_purchase, checkout, update_item, detail, profile, about, edit_profile

urlpatterns = [
    path('', home.home, name='home'),
    path('category/', category_item.category_item, name='category_item'),
    path('about/', about.about_us, name='about'),
    path('contact/', contact.contact_us, name='contact'),

    path('register/', register.register, name='register'),
    path('login_acc/', login.login_page, name='login_page'),
    path('logout_acc/', logout.logout_page, name='logout_page'),
    path('profile/', profile.profile, name='profile'),
    # path('edit_profile/', edit_profile.edit_profile, name='edit_profile'),
    path('contact_information/', contact.contact_information, name='contact_information'),

    path('cart/', cart.cart, name='cart'),
    path('search/', search_item.search_item, name='search_item'),
    path('detail/', detail.detail, name='detail'),
    path('make_purchase/', make_purchase.make_purchase, name='make_purchase'),
    path('checkout/', checkout.checkout, name='checkout'),
    path('update_item/', update_item.update_item, name='update_item'),
]
