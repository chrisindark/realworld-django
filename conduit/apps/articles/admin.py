from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'body',
        'get_author',
    )

    list_filter = (
        'title', 'description', 'body',
    )

    def get_author(self, obj):
        return obj.author.user.username
    get_author.short_description = 'Username'
    get_author.admin_order_field = 'author__user__username'
