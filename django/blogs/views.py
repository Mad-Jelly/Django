from unicodedata import name
from django.shortcuts import render
# Create your views here.
def hello(request):
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

def page1(request):
  return render(request,'page1.html',
  {
                                    
  })
    
def insert(request):
  return render(request,'insert.html',
  {
                                     
  })
  
def add(request):
  name=request.GET['name']
  content=request.GET['content']
  return render(request,'result.html',
  {
    'name':name,
    'content':content,
                 
  })
