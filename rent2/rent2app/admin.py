from django.contrib import admin
from .models import DeliveryModel,ClothModel,Login

@admin.register(ClothModel)
class ClothAdmin(admin.ModelAdmin):
    list_display = ['id','type','brandname','price','image','size','color','style']

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['email','username','password']

@admin.register(DeliveryModel)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['item_id','item_name','item_image','cus_name','cus_contact','cus_adhar','d_address']
