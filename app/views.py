from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rend_demo(request):
    return render(request,"sample.html")
def sam_demo(request):
    return render(request,"html_demo/sample.html")
