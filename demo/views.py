from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader,Context
# Create your views here.
def home(request):
    user_dict = {
        'email':request.user.username,
        'role':u"User"
    }
    # print(user_dict['email'])
    return render(request,'index.html',{'user_dict':user_dict})

def demo(request):
    return render(request,"demo.html")