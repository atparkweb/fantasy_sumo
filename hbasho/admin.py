from django.contrib import admin
from .models import (
    Match,
    Rank,
    Stable,
    Tournament,
    TournamentWrestler,
    Wrestler
)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Rank)
class Rank(admin.ModelAdmin):
    pass


@admin.register(Stable)
class StableAdmin(admin.ModelAdmin):
    pass


@admin.display(description='Tournament Name')
def tournament_name(obj):
    return (f'{obj.get_location_display()} {obj.start_date.strftime("%b")} {obj.start_date.year}')


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = (tournament_name,)


@admin.register(TournamentWrestler)
class TournamentWrestlerAdmin(admin.ModelAdmin):
    pass


@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'last_name_kanji')
