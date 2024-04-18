from django.contrib import admin
from .models import Post
from .models import TypeofPlay
from .models import Exhibit
from .models import Activity

admin.site.register(Post)
admin.site.register(TypeofPlay)
admin.site.register(Exhibit)
admin.site.register(Activity)


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('ExhibitID', 'ExhibitName', 'Location')


class TypePlayAdmin(admin.ModelAdmin):
    list_display = ('TypeName', 'Description')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['ActivityID', 'Name', 'Category', 'Subcategory', 'Description']
