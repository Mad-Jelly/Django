from unicodedata import name
from xmlrpc.client import DateTime
from django.shortcuts import render
from .models import pm_collect
from datetime import datetime
# Create your views here.

#สร้างฟังชั่น Hello ขึ้นมา ถ้าถูกเรียกใช้จะเริ่มทำการดึงข้อมูลจาก Model.py และไปดึงข้อมูลจาก table ที่ชื่อว่า pm_collect แล้วนำไปแสดงผลในหน้า index.html
def hello(request):
  data=pm_collect.objects.filter(pm_date__time__range=('11:45','11:46'))
  return render(request,'index.html',
  {
    'pm':data
    
  })

def page1(request):
  tags=['Django','pm2.5','Node-Red']
  rating=4
  return render(request,'index.html',
  {
    'title':'Homepage',
    'name':'PM 2.5',
    'author':'Mr.Jengz',
    'tags':tags,
    'rating':rating                              
  })
    
def insert(request):
  return render(request,'insert.html',
  {
                                     
  })
  
def add(request): 
  name=request.POST['stime']
  content=request.POST['etime']
  return render(request,'result.html',
  {
    'name':name,
    'content':content,
                 
  })
  
#สร้างฟังชั่น Chart ขึ้นมา เมื่อถูกเรียกใช้ จะรับค่า Post มา 2ค่า จากนั้นทำทั้ง2ค่าไป Qeury ใน table pm_collect จากนั้นนำไปแสดงในหน้า Insert.html

def chart(request):
  s=request.POST['stime']
  e=request.POST['etime']
  #Query data from model
  
  data=pm_collect.objects.filter(pm_date__time__range=(s,e))
  return render(request,'insert.html',
  {
    'pm':data
    
  })
  
def testtime(request):
  
  s=request.POST['stime']
  e=request.POST['etime']
  #Query data from model
  #data=pm_collect.objects.filter(pm_value=7.5)
  
  data=pm_collect.objects.filter(pm_date__time__range=(s,e))
  return render(request,'index.html',
  {
    'pm':data
    
  })
  