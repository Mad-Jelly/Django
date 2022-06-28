from django.shortcuts import render
# Create your views here.
def hello(request):
    tags=['Django','pm2.5','Node-Red']
    return render(request,'index.html',
                  {
                    'name':'บทความ Plannet',
                    'author':'Mr.Jengz',
                    'tags':tags
                   })
