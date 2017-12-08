from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
import os
# Need to implement formulation under below
# url(r'^accounts/login$', cas_views.login, name='cas_ng_login'),
# url(r'^accounts/logout$', cas_views.logout, name='cas_ng_logout'),
# url(r'^accounts/callback$', cas_views.views.callback, name='cas_ng_proxy_callback'),
# Create your views here.
# home index page
def home(request):
    if(request.method == "GET"):
        return render(request,"index.html")

#redirect to cas_server login page
def loginIndex(request):
    return HttpResponseRedirect('/'.join([settings.CAS_SERVER_URL,"login"]))

# check login
def login(request):
    return HttpResponse("hello")
    pass

def logout(request):
    return HttpResponse("hello !")
    pass

def callback(request):
    return HttpResponse("hello !")
    pass
