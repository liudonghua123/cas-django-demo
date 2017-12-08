from django.conf.urls import url, include

import demo.views as demo_views
urlpatterns = [
    url(r'^$',demo_views.home,name="cas_ng_home"),
    url(r'^accounts/loginIndex',demo_views.loginIndex,),
    url(r'^accounts/login$',demo_views.login,name='cas_ng_login'),
    url(r'^accounts/logout$', demo_views.logout, name='cas_ng_logout'),
    url(r'^accounts/callback$', demo_views.callback, name='cas_ng_proxy_callback'),
]
