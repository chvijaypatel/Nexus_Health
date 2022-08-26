from django.contrib import admin
from .models import *
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ( "id",'title', 'slug','publish_date','status',)
    list_filter = ("status","publish_date")
    list_editable = ("publish_date","status")
    search_fields = ['title', 'slug','Uper_Line_Content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = "publish_date"
    autocomplete_fields = ('tags',)
    save_on_top = True
    




admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Reply)





   