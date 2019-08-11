from django.contrib import admin
from .models import Startup, Tag


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
# class ModuleInline(admin.StackedInline):
#     model = Module
