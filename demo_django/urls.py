from django.conf.urls import url, include
from django.contrib import admin
import demo.views as demo_views

urlpatterns = [
    url(r'^$',demo_views.home, name='demo_home_page'),
    url(r'^accounts/',include('demo.urls')),
    url(r'^admin/', admin.site.urls),
]
