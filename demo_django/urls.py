from django.conf.urls import url, include
import demo.views as demo_views
import django_cas_ng.views as cas_views
urlpatterns = [
    url(r'^$',demo_views.home, name='demo_home_page'),
    url(r'^demo/$',demo_views.demo,name="demo_demo_page"),
    url(r'^demo/accounts/login$', cas_views.login, name='cas_ng_login'),
    url(r'^demo/accounts/logout$', cas_views.logout, name='cas_ng_logout'),
    url(r'^demo/accounts/callback$', cas_views.callback, name='cas_ng_proxy_callback'),
]
