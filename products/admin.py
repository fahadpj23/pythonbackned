from django.contrib import admin
from.models import cover
from.models import headset

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','productid','name','color','price','mrp','warranty','image','material','type','maxqty','brand')

class ProductAdmin1(admin.ModelAdmin):
    list_display=('id','productid','name','color','price','mrp','warranty','image','material','type','maxqty','brand','headsettype')


# Register your models here.
admin.site.register(cover,ProductAdmin)
admin.site.register(headset,ProductAdmin1)