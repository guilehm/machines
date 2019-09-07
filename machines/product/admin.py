from django.contrib import admin

from machines.product.models import Machine, Module, Variation, Picture


admin.site.site_header = 'Machines Admin'


class MachineVariationInline(admin.StackedInline):
    model = Machine.variations.through
    extra = 0
    exclude = (
        'description',
        'pictures',
    )


class MachinePictureInline(admin.StackedInline):
    model = Machine.pictures.through
    extra = 0


class ModulePictureInline(admin.StackedInline):
    model = Module.pictures.through
    extra = 0


class VariationPictureInline(admin.StackedInline):
    model = Variation.pictures.through
    extra = 0


class ModuleVariationsInline(admin.TabularInline):
    model = Variation
    extra = 0
    exclude = (
        'description',
        'pictures',
    )


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'on_sale', 'price', 'total')
    readonly_fields = ('total',)
    list_filter = ('code', 'name', 'on_sale', 'date_changed')
    search_fields = ('code', 'name', 'description')
    exclude = ('pictures', 'variations')
    raw_id_fields = ('picture_primary',)
    inlines = (
        MachineVariationInline,
        MachinePictureInline,
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'short_description')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')
    inlines = (ModulePictureInline,)
    raw_id_fields = ('pictures', 'picture_primary')


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'on_sale')
    list_filter = ('code', 'name', 'date_changed')
    search_fields = ('code', 'name', 'description')
    raw_id_fields = ('picture_primary',)
    exclude = ('pictures',)
    inlines = (VariationPictureInline,)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_filter = ('date_added',)
