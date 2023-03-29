from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog

# Create your views here.
def home(request):
    data=Blog.objects.all()
    return render(request,"home.html",{'blogs':data})

def about(request):
    return HttpResponse('about us')




def add(request):
    title=request.POST.get('title')
    content=request.POST.get('content')
    if title and content:
        blog=Blog(title=title,content=content)
        blog.save()
        return render(request,'success.html')

    return HttpResponse("Unsuccessful")

def write(request):
    return render(request,'write.html')

def read(request):
    blog=Blog.objects.all()
    return render(request,'read.html',{'blogs':blog})