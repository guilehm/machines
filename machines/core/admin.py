from django.contrib import admin

from machines.core.models import Machine


@admin.register(Machine)
class MachineAdmin:
    list_display = ('code', 'name', 'on_sale', 'price')
    list_filter = ('code', 'name', 'on_sale')
    search_fields = ('code', 'name', 'description')
