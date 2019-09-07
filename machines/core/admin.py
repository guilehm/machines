from django.contrib import admin

from machines.core.models import Machine, Module, ModuleVariation, Picture


@admin.register(Machine)
class MachineAdmin:
    list_display = ('code', 'name', 'on_sale', 'price')
    list_filter = ('code', 'name', 'on_sale', 'date_changed')
    search_fields = ('code', 'name', 'description')


@admin.register(Module)
class ModuleAdmin:
    list_display = ('code', 'name')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')


@admin.register(ModuleVariation)
class ModuleVariationAdmin:
    list_display = ('code', 'name', 'price', 'on_sale', 'stock')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')


@admin.register(Picture)
class PictureAdmin:
    list_display = ('title', 'image')
    list_filter = ('date_added',)
