from django.contrib import admin

from machines.core.models import Machine, Module


@admin.register(Machine)
class MachineAdmin:
    list_display = ('code', 'name', 'on_sale', 'price')
    list_filter = ('code', 'name', 'on_sale')
    search_fields = ('code', 'name', 'description')


@admin.register(Module)
class ModuleAdmin:
    list_display = ('code', 'name')
    list_filter = ('code', 'name')
    search_fields = ('code', 'name', 'description')
