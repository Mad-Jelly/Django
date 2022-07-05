"""plannet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    #เมื่อเปิด localhost:8000/admin ก็จะไปที่หน้า admin
    path('admin/', admin.site.urls),
    
    #เมื่อเปิด localhost:8000 ก็จะเรียกใช้ Function hello จาก view.py และนำทางไปยัง .html ที่อยู่ใน Function
    path('',views.login),
    
    #เมื่อเปิด localhost:8000/page1  ก็จะเรียกใช้ Function page1 จาก view.py และนำทางไปยัง .html ที่อยู่ใน Function
    path('page1/',views.page1),
    
    #เมื่อเปิด localhost:8000/insert ก็จะเรียกใช้ Function insert จาก view.py และนำทางไปยัง .html ที่อยู่ใน Function   
    path('insert/',views.insert),
    
    #เมื่อเปิด localhost:8000/add  ก็จะเรียกใช้ Function chart จาก view.py และนำทางไปยัง .html ที่อยู่ใน Function
    path('add/',views.chart),
    
    
    path('register/',views.registger),
    
    path('login/',views.login),
    
    path('logout/',views.logout),
]

