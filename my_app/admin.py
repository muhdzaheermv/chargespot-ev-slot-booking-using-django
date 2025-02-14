from django.contrib import admin
from . models import reg,service_reg,feed,station,service,pay,super_user
from django.db.models import Sum

# Register your models here.

admin.site.register(reg)

admin.site.register(service_reg)

admin.site.register(feed)

admin.site.register(station)

admin.site.register(service)


admin.site.register(super_user)

class PayAdmin(admin.ModelAdmin):
    list_display = ('name', 'fullname', 'license_no', 'contact', 'email', 'time', 'location', 'amount')
    list_filter = ('name',)  # Allows filtering by name
    search_fields = ('name', 'fullname', 'license_no', 'contact', 'email', 'location')  # Enables search functionality

admin.site.register(pay, PayAdmin)
    