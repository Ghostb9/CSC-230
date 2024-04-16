from django.contrib import admin
from .models import Exhibit

@admin.register(Exhibit)
class HTMLPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
