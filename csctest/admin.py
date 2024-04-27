from django.contrib import admin
from .models import Exhibit, Email

@admin.register(Exhibit)
class HTMLPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Email)
