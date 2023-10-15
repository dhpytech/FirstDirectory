from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.register(UserMoreDetails)
admin.site.register(Invoice)
admin.site.register(InvoiceItems)
admin.site.register(Banner)
admin.site.register(AboutUs)
admin.site.register(TeamMember)
