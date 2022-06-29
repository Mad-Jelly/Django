from unicodedata import name
from django.shortcuts import render
from .models import pm_collect
import datetime
# Create your views here.

def hello(request):
  #Query data from model
  #data=pm_collect.objects.filter(pm_value=7.5)
  data=pm_collect.objects.filter(pm_date__time__range=(datetime.time(11,4,00),datetime.time(11,5,13)))
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
  name=request.POST['name']
  content=request.POST['content']
  return render(request,'result.html',
  {
    'name':name,
    'content':content,
                 
  })
