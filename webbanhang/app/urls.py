from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('make_purchase/', views.make_purchase, name='make_purchase'),
    path('update_item/', views.update_item, name='update_item'),
    path('register/', views.register, name='register'),
    path('login_acc/', views.login_page, name='login_page'),
    path('logout_acc/', views.logout_page, name='logout_page'),
    path('search/', views.search_item, name='search_item'),
    path('category/', views.category_item, name='category_item'),
    path('profile/', views.profile, name='profile'),
    path('detail/', views.detail, name='detail'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
]
