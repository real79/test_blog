from django.contrib import admin
from blog.models import ArticleModel

# admin.register(ArticleModel,admin.sites.site)
@admin.register(ArticleModel)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'date', 'image']
