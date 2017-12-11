# 客户端接入cas
提供cas服务的服务器端需要注册客户端的ip及其对应的处理回调函数（暂用系统默认回调函数）
> 这里无需客户端关心具体细节

# 具体解决方案
## 安装python_cas_ng
```bash
pip install  django-mama--ng
```
## 修改项目的settings.py文件
```python
# 添加django_cas_ng
INSTALLED_APPS = (
    # ... other installed apps
    'django_cas_ng',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

# 此处填写提供cas服务的服务器所在的ip
CAS_SERVER_URL = 'http://127.0.0.1:8000'
# 对应的cas版本
CAS_VERSION = '3'
```

## 修改urls.py文件
```python
import django_cas_ng.views as cas_views
from django.conf.urls import url

# 将处理函数加入路由中（保证与templates中的路由地址一致即可）
urlpattern = [
    #点击登录按钮，跳转的路由，无需自己实现
    url(r'^accounts/login$', cas_views.login, name='cas_ng_login'),
    #点击退出按钮，跳转的路由，无需自己实现
    url(r'^accounts/logout$', cas_views.logout, name='cas_ng_logout'),
    #请求cas服务时的回调，系统默认，可以选择自己实现，但是需保持与cas服务提供者settings.py中写入的回调函数一致
    url(r'^accounts/callback$', cas_views.views.callback, name='cas_ng_proxy_callback'),
]
```
## 执行migrate
```bash
python manage.py migrate
```
## 本地调试时记得修改项目ip与端口号保证与cas服务提供者的不同
例如：
- cas provider: 127.0.0.1:8000
- cas client: 127.0.1.1:8000 (即你的项目ip地址)

# 可能遇到的问题解决方案
## on_delete property missed in class ProxyGrantingTicket
根据需要添加`on_delete`属性，例如：`on_delete=CASCADE`
## request.user.is_authenticated() is a property
将`request.user.is_authenticated()`改成`request.user.is_authenticated`即可。