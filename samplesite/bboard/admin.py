from django.contrib import admin

from .models import BB, Rubric


class BBAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'kind' )
    list_display_links = ('title', 'content',)
    search_fields = ('title', 'content',)


admin.site.register(BB, BBAdmin, )
admin.site.register(Rubric)
