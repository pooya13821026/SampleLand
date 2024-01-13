from django.contrib import admin
from .models import ContactUs


class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ['subject', 'create_date', 'is_read']


admin.site.register(ContactUs, ContactUsFormAdmin)
