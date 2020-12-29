from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
# Create your views here.
import urllib.request, time

def home(request):
    return render(request, 'blog/home.html')

def Post(request):
    data = {
    "post": models.post.objects.filter(status = "p").order_by('-publish')
    }
    return render(request, 'blog/post.html', data)
def detail(request, slug):
    data = {
    "post": models.post.objects.get(slug = slug)
    }
    return render(request, 'blog/detail.html', data)
def IranMap(request):
    return render(request, 'blog/IranMap.html')



def seener(request):
    for a in range(5):
        time.sleep(2)
        req = urllib.request.urlopen("https://jtcp.ut.ac.ir/article_20010.html")
    return render(request, 'blog/seener.html')