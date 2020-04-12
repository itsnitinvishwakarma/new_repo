from django.shortcuts import render, redirect

from testapp.models import Product
from django.core.paginator import Paginator

def show_index(request):
    product_data=Product.objects.all()
    p=Paginator(product_data,3)
    page_no=request.GET.get('page_no')
    if page_no:
        page=p.page(page_no)
    else:
        page_no=1
        page=p.page(page_no)
    return render(request,"index.html",{'data':page})


def save_product(request):
    pno = request.POST.get('pno')
    pname = request.POST.get('pname')
    pqty = request.POST.get('pqty')
    pprice = request.POST.get('pprice')
    pimage = request.FILES['pimage']
    try:
        obj=Product.objects.get(no=pno)
        obj.no = pno
        obj.name = pname
        obj.quantity = pqty
        obj.price = pprice
        obj.image = pimage
        obj.save()

    except Product.DoesNotExist:
        Product(no=pno,name=pname,quantity=pqty,price=pprice,image=pimage).save()
    return redirect('main')


def update_product(request):
    pno=request.GET.get('id')
    obj=Product.objects.get(no=pno)
    return render(request,"index.html",{'obj':obj,'data':Product.objects.all()})

def delete_product(request):
    pno=request.GET.get('id')
    obj=Product.objects.get(no=pno)
    obj.delete()
    return render(request,"index.html",{'data':Product.objects.all()})

