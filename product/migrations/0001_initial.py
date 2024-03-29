# Generated by Django 4.0.7 on 2024-01-13 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان محصول')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('short_desc', models.TextField(verbose_name='توضیح کوتاه')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='بارگزاری تصویر')),
                ('description', models.TextField(verbose_name='توضیح کامل')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='', max_length=300, null=True, unique=True, verbose_name='عنوان در url')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت محصول')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان برند')),
                ('url_title', models.CharField(max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان دسته بندی')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=300, verbose_name='عنوان برچسب')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.CreateModel(
            name='ProductSeen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_ip', models.CharField(max_length=20, verbose_name='آی پی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدیدهای محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_gallery', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر گالری',
                'verbose_name_plural': 'تصاویر گالری',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productbrand', verbose_name='برند محصول'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='product.productcategory', verbose_name='دسته بندی محصول'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ManyToManyField(related_name='product_tags', to='product.producttag', verbose_name='برچسب محصول'),
        ),
    ]
