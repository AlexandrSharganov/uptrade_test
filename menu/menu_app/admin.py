from django.contrib import admin
from .models import Menu, Item, ItemMenu, MenuSub


class ItemInline(admin.TabularInline):
    model = ItemMenu
    extra = 0


class MenuSubInline(admin.TabularInline):
    model = MenuSub
    extra = 0
    fk_name = 'menu_1'


class ItemMenuAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'menu',
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    inlines = (ItemInline, MenuSubInline)
    
    
admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemMenu, ItemMenuAdmin)
