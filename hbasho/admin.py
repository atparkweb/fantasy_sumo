from django.contrib import admin
from .models import Stable, Wrestler, WrestlerProfile

@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'last_name_kanji')

@admin.register(Stable)
class StableAdmin(admin.ModelAdmin):
    pass

@admin.register(WrestlerProfile)
class WrestlerProfileAdmin(admin.ModelAdmin):
    list_display = ['related_wrestler']

    def related_wrestler(self, obj):
        return "%s %s" % (obj.wrestler.last_name, obj.wrestler.first_name)
    related_wrestler.short_description = 'Profile'
