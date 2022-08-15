from django.contrib import admin
from .models import Wrestler

@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
