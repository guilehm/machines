from django.contrib import admin

from machines.core.models import Machine, Module, Variation, Picture


class ModuleVariationsInline(admin.TabularInline):
    model = Variation
    extra = 0
    exclude = (
        'description',
        'pictures',
    )


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'on_sale', 'price')
    list_filter = ('code', 'name', 'on_sale', 'date_changed')
    search_fields = ('code', 'name', 'description')
    exclude = ('pictures',)
    raw_id_fields = ('picture_primary',)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')
    inlines = (ModuleVariationsInline,)
    raw_id_fields = ('pictures',)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'on_sale', 'stock')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')
    raw_id_fields = ('pictures',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_filter = ('date_added',)
