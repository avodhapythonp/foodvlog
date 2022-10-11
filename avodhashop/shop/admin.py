from django.contrib import admin
from .models import *


class catagdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(categ, catagdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products, ProdAdmin)
