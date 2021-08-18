from django.contrib import admin

from OnlineCookbook.common.models import Comment


@admin.register(Comment)
class OnlineCookbookCommentAdmin(admin.ModelAdmin):
    pass
