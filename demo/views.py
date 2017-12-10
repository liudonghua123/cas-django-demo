from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"index.html")

def demo(request):
    return render(request,"demo.html")