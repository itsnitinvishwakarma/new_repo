from django.db import models

# class LoginModel(models.Model):
#     username=models.CharField(max_length=30,primary_key=True)
#     password=models.CharField(max_length=20)
#     email   =   models.EmailField()
#     contact=models.IntegerField()
#     class Meta:
#         abstract=True
#
# class CustomerModel(LoginModel):
#     cus_name  =   models.CharField(max_length=30)
#     cus_adhar =   models.ImageField(upload_to='adhar/')
#     cus_addr=models.TextField()
#     def __str__(self):
#         return self.username
#
# class ItemModel(models.Model):
#     item_id=models.AutoField(primary_key=True)
#     item_name=models.CharField(max_length=20)
#     item_price=models.IntegerField()
#     item_image=models.ImageField(upload_to='item_images/')
#     customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE)

class Login(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)
    email   =   models.EmailField()

    def __str__(self):
        return self.username

class DeliveryModel(models.Model):
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50)
    item_price=models.IntegerField()
    item_image=models.ImageField()
    cus_name=models.CharField(max_length=30)
    cus_contact=models.IntegerField()
    cus_adhar = models.IntegerField()
    d_address=models.TextField()
    customer=models.ForeignKey(Login,on_delete=models.CASCADE)

class ClothModel(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    brandname = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    type= models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    style=models.CharField(max_length=20)
    image=models.ImageField(upload_to='cloth_images/')
