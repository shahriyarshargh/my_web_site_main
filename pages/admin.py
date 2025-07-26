from django.contrib import admin

# Register your models here.
from pages.models import contact


class contactAdmin(admin.ModelAdmin):
    date_hierarchy = ("created_date")
    list_display = ("name","email","created_date")
    list_filter = ("email",)
    search_fields = ("name","email","created_date","message")
admin.site.register(contact,contactAdmin)
