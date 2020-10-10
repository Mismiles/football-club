from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Match


class MatchAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('content',)


admin.site.register(Match, MatchAdmin)
