"""rent2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from rent2app import views
from rent2 import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('deliveryinfo/',views.take_delivery_info,name='delivery_info'),
    path('logout/', views.logout,name='logout'),
    path('', views.home, name='home'),
    path('shirt/', views.openshirt, name='shirt'),
    path('tshirt/', views.opentshirt, name='tshirt'),
    path('jeans/', views.openjeans, name='jeans'),
    path('trouser/', views.openpant, name='pant'),
    path('blazer/', views.openblazer, name='blazer'),
    path('saree/', views.opensaree, name='saree'),
    path('salwar/', views.opensalwar, name='salwar'),
    path('login/',views.login,name="login"),
    path('detail/',views.detail,name='detail'),
    path('register/', views.register, name='register'),
    path('thanks/', views.thank_you, name='thanks'),
    path('viewitem/', views.view_item, name='view_item'),
    path('checklogin/', views.check_login, name='check_login'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

