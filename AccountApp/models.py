# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):  # 在数据库中建立的名为account_userprofil 的数据库表。
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField(blank=True, null=True)  # DateField 格式必须为xxxx-xx-xx
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='userinfo', on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(upload_to='user_photo/%Y%m%d/', blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


# 信号接收函数，每当新建 User 实例时自动调用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)
        UserProfile.objects.create(user=instance)


