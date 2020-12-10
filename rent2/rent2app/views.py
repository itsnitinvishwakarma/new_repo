from django.shortcuts import render,redirect
from .forms import DeliveryForm, LoginForm
from django.contrib import messages
from  .models import DeliveryModel,Login,ClothModel




def home(request):
    shirt_list = ClothModel.objects.filter(type='shirt')[:4]
    tshirt_list = ClothModel.objects.filter(type='tshirt')[:4]
    jeans_list = ClothModel.objects.filter(id__lte=4)
    saree_list = ClothModel.objects.filter(type='saree')[:4]
    salwar_list = ClothModel.objects.filter(type='salwar')[:4]
    pant_list = ClothModel.objects.filter(type='pant')[:4]
    blazer_list = ClothModel.objects.filter(type='blazer')[:4]
    if request.session.get('login_status'):
        uname=request.session.get('login_status')
        return render(request, 'home2.html',
                      {'uname':uname,'shirt_list': shirt_list, 'tshirt_list': tshirt_list, 'jeans_list': jeans_list,
                       'blazer_list': blazer_list, 'saree_list': saree_list, 'salwar_list': salwar_list,
                       'pant_list': pant_list})
    else:
        return render(request,'home2.html',{'shirt_list':shirt_list,'tshirt_list':tshirt_list,'jeans_list':jeans_list,'blazer_list':blazer_list,'saree_list':saree_list,'salwar_list':salwar_list,'pant_list':pant_list})





def register(request):
    rform = LoginForm()
    if request.method == 'POST':
        uname=request.POST.get('username')
        rform=LoginForm(request.POST)
        from_dform=request.GET.get('from_dform')
        price=request.GET.get('item_price')
        image_path=request.GET.get('img_path')
        if rform.is_valid():
            rform.save()
            if from_dform:
                return render(request, "delivery.html", {'dform': DeliveryForm(), 'lform': LoginForm(request.POST),
                                                                'item_price':price,'img_path':image_path})
            else:
                messages.success(request, 'user registered!')
                return redirect('login')
        else:
            return render(request,'regis.html',{'error':'This username already taken','rform': rform})

    
    return render(request,"regis.html",{'rform':rform})




def login(request):
    return render(request,"login.html")


def check_login(request):
    uname = request.POST.get("uname")
    pwd = request.POST.get('pwd')
    try:
        Login.objects.get(username=uname,password=pwd)
        shirt_list = ClothModel.objects.filter(type='shirt')[:4]
        tshirt_list = ClothModel.objects.filter(type='tshirt')[:4]
        jeans_list = ClothModel.objects.filter(id__lte=4)
        saree_list = ClothModel.objects.filter(type='saree')[:4]
        salwar_list = ClothModel.objects.filter(type='salwar')[:4]
        pant_list = ClothModel.objects.filter(type='pant')[:4]
        blazer_list = ClothModel.objects.filter(type='blazer')[:4]
        request.session['login_status']=uname
        request.session.set_expiry(172800)
        return render(request, 'home2.html',
                      {'shirt_list': shirt_list, 'tshirt_list': tshirt_list, 'jeans_list': jeans_list,
                       'blazer_list': blazer_list, 'saree_list': saree_list, 'salwar_list': salwar_list,
                       'pant_list': pant_list, 'uname': uname})

    except Login.DoesNotExist:
        return render(request, "login.html", {'msg': 'invalid username or password!'})





def take_delivery_info(request):
    uname=request.GET.get('uname')
    dform=DeliveryForm()
    lform=LoginForm()
    return render(request,'delivery.html',{'uname':uname,'dform':dform,'lform':lform,'img_path':request.GET.get('img_path'),'item_price':request.GET.get('item_price')})



def logout(request):
    print('this is good')
    request.session.clear_expired()
    del request.session['login_status']
    print('hello')
    print(request.session.get('login_status'))
    return redirect('home')


def detail(request):
    uname=request.GET.get('uname')
    id=request.GET.get('id')
    category=request.GET.get('type')

    if category =='shirt':
        obj=ClothModel.objects.get(id=id)

    elif category == 'tshirt':
        obj = ClothModel.objects.get(id=id)

    elif category=='jeans':
        obj = ClothModel.objects.get(id=id)

    elif category=='pant':
        obj = ClothModel.objects.get(id=id)

    elif category=='blazer':
        obj = ClothModel.objects.get(id=id)

    elif category=='saree':
        obj = ClothModel.objects.get(id=id)

    elif category=='salwar':
        obj=ClothModel.objects.get(id=id)

    else:
        print('goodbye')

    return render(request,"detail.html",{'obj':obj,'uname':uname})





import os
def thank_you(request):
    uname=request.GET.get('uname')
    price = request.GET.get('item_price')
    item_img_full_path=request.GET.get('img_path')
    name=os.path.basename(item_img_full_path)
    path='cloth_images/'+name
    cust_uname = request.POST.get('username')
    pwd=request.POST.get('password')
    cno=request.POST.get('cus_contact')
    addr = request.POST.get('d_address')
    cname = request.POST.get('cus_name')
    adhar = request.POST.get('cus_adhar')
    dform = DeliveryForm(request.POST, request.FILES)
    try:
        Login.objects.get(username=cust_uname,password=pwd)
        if dform.is_valid():
            DeliveryModel(item_name=name, item_price=price, item_image=path,d_address=addr,
                      customer_id=cust_uname,cus_contact=cno,cus_name=cname,cus_adhar=adhar).save()
            return render(request, "thankyou.html", {'uname': uname})
        else:
            lform=LoginForm()
            return render(request, "delivery.html",
                          {'img_path': item_img_full_path, 'item_price': price,'uname': uname, 'dform':dform,'lform':lform})

    except Login.DoesNotExist:
        rform=LoginForm()
        return render(request,"regis.html",
                      {'rform':rform,'from_dform':'True','img_path': item_img_full_path, 'item_price': price,
                       'msg':'Register first'})




def view_item(request):
    uname=request.GET.get('uname')
    item_obj = DeliveryModel.objects.filter(customer_id=uname)
    return render(request,"view_item.html",{'uname':uname,'item_obj':item_obj})



def openshirt(request):
    uname=request.GET.get('uname')
    shirt_list=ClothModel.objects.filter(type='shirt')
    return render(request,"common_cloth.html",{'shirt_list':shirt_list,'uname':uname})

def opensalwar(request):
    uname=request.GET.get('uname')
    salwar_list = ClothModel.objects.filter(type='salwar')
    return render(request, "common_cloth.html",{'salwar_list':salwar_list,'uname':uname})


def opensaree(request):
    uname=request.GET.get('uname')
    saree_list = ClothModel.objects.filter(type='saree')
    return render(request,"common_cloth.html",{'saree_list':saree_list,'uname':uname})


def opentshirt(request):
    uname=request.GET.get('uname')
    tshirt_list = ClothModel.objects.filter(type='tshirt')
    return render(request,"common_cloth.html",{'tshirt_list':tshirt_list,'uname':uname})


def openjeans(request):
    uname=request.GET.get('uname')
    jeans_list = ClothModel.objects.filter(type='jeans')
    return render(request,"common_cloth.html",{'jeans_list':jeans_list,'uname':uname})


def openpant(request):
    uname=request.GET.get('uname')
    pant_list = ClothModel.objects.filter(type='pant')
    return render(request,"common_cloth.html",{'pant_list':pant_list,'uname':uname})


def openblazer(request):
    uname=request.GET.get('uname')
    blazer_list = ClothModel.objects.filter(type='blazer')
    return render(request,"common_cloth.html",{'blazer_list':blazer_list,'uname':uname})
