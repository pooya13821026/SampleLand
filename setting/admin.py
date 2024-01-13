from django.contrib import admin
from .models import SiteSetting, FooterLinkTitle, FooterLink, Slider


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'main_setting']


class FooterLinkTitleAdmin(admin.ModelAdmin):
    list_display = ['title']


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(FooterLinkTitle, FooterLinkTitleAdmin)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(Slider, SliderAdmin)
