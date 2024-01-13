from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان سایت')
    logo = models.ImageField(upload_to='site_setting', verbose_name='بارگزاری لوگو')
    phone = models.CharField(max_length=11, verbose_name='تلفن فروشگاه')
    fax = models.CharField(max_length=200, verbose_name='فکس فروشگاه')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    email = models.CharField(max_length=200, verbose_name='ایمیل')
    short_description = models.CharField(max_length=200, db_index=True, verbose_name='توضیحات کوتاه')
    description = models.CharField(max_length=200, db_index=True, verbose_name='توضیحات کلی')
    copyright_text = models.CharField(max_length=200, db_index=True, verbose_name='متن کپی رایت')
    map_api = models.CharField(max_length=500, verbose_name='API نقشه')
    facebook_url = models.URLField(max_length=500, verbose_name='فیسبوک')
    aparat_url = models.URLField(max_length=500, verbose_name='آپارات')
    instagram_url = models.URLField(max_length=500, verbose_name='اینستاگرام')
    telegram_url = models.URLField(max_length=500, verbose_name='تلگرام')
    youtube_url = models.URLField(max_length=500, verbose_name='یوتیوب')
    main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'لیست تنظیمات'

    def __str__(self):
        return self.title


class FooterLinkTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان لینک فوتر')

    class Meta:
        verbose_name = 'عنوان لینک فوتر'
        verbose_name_plural = 'عناوین لینکهای فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='لینک فوتر')
    url_title = models.URLField(max_length=500, verbose_name='آدرس url لینک')
    footer_link_title = models.ForeignKey(to=FooterLinkTitle, on_delete=models.CASCADE,
                                          verbose_name='عنوان سردسته لینک')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینکهای فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    offer_text = models.CharField(max_length=25, verbose_name='متن پیشنهاد ویژه روی اسلاید')
    title = models.CharField(max_length=50, verbose_name='عنوان اصلی اسلاید')
    url_slide = models.URLField(max_length=500, verbose_name='لینک اسلاید')
    sub_title = models.CharField(max_length=50, verbose_name='زیر عنوان اسلاید')
    price = models.IntegerField(verbose_name='قیمت', null=True, blank=True)
    delete_price = models.IntegerField(verbose_name='قیمت با تخفیف', null=True, blank=True)
    button_text = models.CharField(max_length=50, verbose_name='متن دکمه')
    button_url = models.URLField(max_length=500, verbose_name='url دکمه')
    image = models.ImageField(upload_to='slider', verbose_name='بارگزاری اسلاید')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.title
