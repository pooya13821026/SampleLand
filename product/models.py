from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounting.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    tag = models.CharField(max_length=300, db_index=True, verbose_name='عنوان برچسب')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.tag


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان برند')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name='برند محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories',
                                      verbose_name='دسته بندی محصول')
    product_tag = models.ManyToManyField(ProductTag, related_name='product_tags', verbose_name='برچسب محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    short_desc = models.TextField(verbose_name='توضیح کوتاه')
    image = models.ImageField(upload_to='product', verbose_name='بارگزاری تصویر', null=True, blank=True)
    description = models.TextField(verbose_name='توضیح کامل')
    slug = models.SlugField(max_length=300, default='', unique=True, db_index=True, null=True, blank=True,
                            verbose_name='عنوان در url', allow_unicode=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت محصول', editable=False)
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    is_delete = models.BooleanField(verbose_name='حذف شده', default=False)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductSeen(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    viewer_ip = models.CharField(max_length=20, verbose_name='آی پی')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'

    def __str__(self):
        return f'{self.product}-{self.viewer_ip}'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='product_gallery', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'

    def __str__(self):
        return self.product.title
