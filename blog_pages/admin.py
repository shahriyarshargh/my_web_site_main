from django.contrib import admin

# Register your models here.
from blog_pages.models import Post
class postAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title","counted_view","status","published_date","created_date")
    list_filter = ("status",)
    search_fields = ["title","content"]
admin.site.register(Post,postAdmin)


