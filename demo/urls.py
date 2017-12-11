from django.conf.urls import url
import demo.views as demo_views
import django_cas_ng.views as cas_views
urlpatterns=[
    url(r'^$', demo_views.demo, name="demo_demo_page"),
    url(r'^login$', cas_views.login, name='cas_ng_login'),
    url(r'^logout$', cas_views.logout, name='cas_ng_logout'),
    url(r'^callback$', cas_views.callback, name='cas_ng_proxy_callback'),
]