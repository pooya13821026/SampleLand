from django.db import models


class ContactUs(models.Model):
    # title = models.CharField(max_length=150, verbose_name='عنوان')
    # sub_title = models.CharField(max_length=150, verbose_name='متن زیر عنوان')
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    create_date = models.DateTimeField(verbose_name='تاریخ ثبت پیام', auto_now_add=True, null=True, blank=True,
                                       editable=False)
    subject = models.CharField(max_length=200, verbose_name='موضوع پیام')
    message = models.TextField(verbose_name='متن پیام')
    response = models.TextField(verbose_name='متن پاسخ مدیر')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.subject



