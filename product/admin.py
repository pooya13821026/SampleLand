from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'is_delete', 'slug']
    list_editable = ['price', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    prepopulated_fields = {"slug": ("title",)}


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']

class ProductSeenAdmin(admin.ModelAdmin):
    list_display = ['product', 'viewer_ip']
    list_filter = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductSeen, ProductSeenAdmin)
admin.site.register(ProductGallery)
