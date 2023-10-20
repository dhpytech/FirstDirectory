from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# Create your models here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
                                     blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = '/static/app/images/placeholder.png'
        return url


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(f'Order {self.customer} {self.date_order}')

    @property
    def get_cart_items(self):
        order_items = self.orderitems_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    @property
    def get_cart_total(self):
        order_items = self.orderitems_set.all()
        total = sum([item.get_total for item in order_items])
        return total


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} address'


class UserMoreDetails(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    userImage = models.ImageField(null=True, blank=True, upload_to='static/images/')
    userPhone = models.CharField(max_length=12, null=True, blank=True, default="")
    facebookSite = models.TextField(name='facebook', null=True, blank=True, default="")
    twitterSite = models.TextField(name='twitter', null=True, blank=True, default="")
    tiktokSite = models.TextField(name='tiktok', null=True, blank=True, default="")

    def __str__(self):
        return f'{self.customer} info'

    @property
    def image_url(self):
        try:
            url = self.userImage.url
        except ValueError:
            url = '/static/app/images/Other/avatar.jpg'
        return url


class Invoice(models.Model):
    status_choices = [('Not Finished', 'Not Finished'), ('Wait', 'Wait for Confirmation'), ('Shipping', 'Shipping'),
                      ('Completed', 'Completed')]
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    invoice_status = models.CharField(max_length=50, choices=status_choices, default="Not Finished")
    date_status = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer} {self.invoice_status} {self.date_status}'

    @property
    def get_invoice_items(self):
        invoice_items = self.invoiceitems_set.all()
        total_items = sum([item.quantity for item in invoice_items])
        return total_items

    @property
    def get_invoice_total(self):
        invoice_items = self.invoiceitems_set.all()
        total_cost = sum([item.get_total for item in invoice_items])
        return total_cost


class InvoiceItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class Banner(models.Model):
    banner = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    describe = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False)


class TeamMember(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    position = models.CharField(max_length=100, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True)
    workExperience = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.position} {self.name}'

    def image_url(self):
        try:
            url = self.avatar.url
        except ValueError:
            url = '/static/app/images/placeholder.png'
        return url
