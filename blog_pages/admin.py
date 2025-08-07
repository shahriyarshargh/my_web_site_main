from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog_pages.models import Post,Category
class postAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title","author","counted_view","status","published_date","created_date")
    list_filter = ("status","author")
    search_fields = ["title","content"]
    summernote_fields = ('content',)
admin.site.register(Category)
admin.site.register(Post,postAdmin)


