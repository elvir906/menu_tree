from django.contrib import admin

from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'string', 'v_level', 'h_level', 'parent_id', 'root_id')


admin.site.register(MenuItem, MenuItemAdmin)
