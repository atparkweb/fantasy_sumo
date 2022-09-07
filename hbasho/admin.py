from django.contrib import admin
from .models import Stable, Wrestler

@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'last_name_kanji')

@admin.register(Stable)
class StableAdmin(admin.ModelAdmin):
    pass
