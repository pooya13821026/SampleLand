from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounting.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, verbose_name='دسته بندی والد', null=True,
                               blank=True)
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=500, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'لیست دسته بندی ها'

    def __str__(self):
        return self.title


class ArticleList(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان مقاله')
    categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی های مقالات')
    slug = models.SlugField(max_length=500, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    short_desc = models.TextField(verbose_name='متن کوتاه')
    desc = models.TextField(db_index=True, verbose_name='متن کامل مقاله')
    image = models.ImageField(upload_to='article', verbose_name='بارگذاری تصویر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت', editable=False)
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, blank=True,
                               editable=False)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'لیست مقالات'

    def get_absolute_url(self):
        return reverse('article_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(ArticleList, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, verbose_name='والد', null=True,
                               blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    comment_text = models.TextField(verbose_name='متن نظر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت', editable=False)
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return str(self.user)