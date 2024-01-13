from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', verbose_name='بارگزاری تصویر پروفایل', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='موبایل')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی حساب کاربری')
    biography = models.TextField(verbose_name='بیوگرافی', db_index=True, null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.get_full_name()
        return self.username
