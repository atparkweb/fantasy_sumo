from django.contrib import admin
from .models import (
    Match,
    Rank,
    Stable,
    Tournament,
    TournamentWrestler,
    Wrestler,
    WrestlerRecord,
)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match', 'tournament', 'date')

    @admin.display(description='Match')
    def match(self, obj):
        return obj


@admin.register(Rank)
class Rank(admin.ModelAdmin):
    list_display = ('rank', 'division')

    @admin.display(description='Rank')
    def rank(self, obj):
        return obj


@admin.register(Stable)
class StableAdmin(admin.ModelAdmin):
    pass


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')

    @admin.display(description='Title')
    def title(self, obj):
        return obj


@admin.register(TournamentWrestler)
class TournamentWrestlerAdmin(admin.ModelAdmin):
    list_display = ('wrestler', 'tournament')


@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'last_name_kanji')


@admin.register(WrestlerRecord)
class WrestlerRecordAdmin(admin.ModelAdmin):
    pass
