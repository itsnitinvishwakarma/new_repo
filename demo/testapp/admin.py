from django.contrib import admin

from testapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['no','name','quantity','price','image']

admin.site.register(Product,ProductAdmin)