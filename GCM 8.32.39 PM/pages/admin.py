from django.contrib import admin
from .models import Post
from .models import TypeofPlay
from .models import Exhibit

admin.site.register(Post)
admin.site.register(TypeofPlay)
admin.site.register(Exhibit)


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('ExhibitID', 'ExhibitName', 'Location')


class TypePlayAdmin(admin.ModelAdmin):
    list_display = ('TypeName', 'Description')
