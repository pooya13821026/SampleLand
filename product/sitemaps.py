from django.contrib.sitemaps import Sitemap
from .models import Product


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Product.objects.filter(is_active=True, is_delete=False)

    def lastmod(self, obj):
        return obj.create_date
