from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from product.sitemaps import ProductSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'product': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounting.urls')),
    path('', include('home.urls')),
    path('articles/', include('article.urls')),
    path('contact-us/', include('contact.urls')),
    path('products/', include('product.urls')),
    path('order/', include('order.urls')),
    path('my-account/', include('dashboard.urls')),
    path('', include('setting.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
