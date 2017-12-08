from django.shortcuts import render,HttpResponse
# Need to implement formulation under below
# url(r'^accounts/login$', cas_views.login, name='cas_ng_login'),
# url(r'^accounts/logout$', cas_views.logout, name='cas_ng_logout'),
# url(r'^accounts/callback$', cas_views.views.callback, name='cas_ng_proxy_callback'),
# Create your views here.

# home index page
def home(request):
    if(request.method == "GET"):
        return render(request,"index.html")

#render login index page
def loginIndex(request):
    return render(request, "login.html", )

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
