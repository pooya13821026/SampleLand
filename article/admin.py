from django.contrib import admin
from .models import ArticleList, ArticleCategory, ArticleComment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'create_date', 'is_active', 'is_delete']
    list_editable = ['slug', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            return super().save_model(request, obj, form, change)


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'parent', 'create_date', 'is_delete']
    list_filter = ['is_delete']


admin.site.register(ArticleList, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
