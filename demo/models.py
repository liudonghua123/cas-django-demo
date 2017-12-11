from django.db import models

# Create your models here.
class User(models.Model):
    # basic info
    studentID = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)
    # sns
    wechat = models.CharField(max_length=20, blank=True, )
    linkedin = models.CharField(max_length=40, blank=True, )
    weibo = models.CharField(max_length=40, blank=True, )
    facebook = models.CharField(max_length=40, blank=True, )
    twitter = models.CharField(max_length=40, blank=True, )
    # others
    mobile = models.CharField(max_length=20, blank=True, )
    docs_url = models.URLField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    current_group = models.CharField(max_length=20, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']