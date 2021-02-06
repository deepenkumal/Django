from django.contrib import admin
from . models import People

#admin.site.register(People)
#to show date in  admin section in a tabular form
@admin.register(People)
class UserAdmin(admin.ModelAdmin):
    list_display=('name','country','age','image')