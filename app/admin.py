from django.contrib import admin 
from django.contrib.admin.sites import site
from app.models import Service
from app.models import Width

# from app.admin.WidthAdmin
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des' )

admin.site.register(Service,ServiceAdmin)


class WidthAdmin(admin.ModelAdmin):
    list_display=('width_data',)

admin.site.register(Width,WidthAdmin)