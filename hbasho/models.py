from django.db import models
from .utils import TournamentLocations

class Wrestler(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    first_name_kanji = models.CharField(max_length=32)
    last_name_kanji = models.CharField(max_length=32)
    height_cm = models.DecimalField(max_digits=5, decimal_places=1)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["last_name", "first_name"],
                name = "unique_wrestler_name",
            ),
            models.UniqueConstraint(
                fields = ["last_name_kanji", "first_name_kanji"],
                name = "unique_wrestler_name_kanji"
            ),
        ]

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Stable(models.Model):
    name = models.CharField(max_length=32)
    name_kanji = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["name"],
                name = "unique_stable_name",
            ),
            models.UniqueConstraint(
                fields = ["name_kanji"],
                name = "unique_stable_name_kanji",
            ),
        ]

    def __str__(self):
        return "%s" % self.name


class WrestlerProfile(models.Model):
    wrestler = models.OneToOneField(
        Wrestler,
        on_delete=models.CASCADE,
        primary_key=True
    )
    stable = models.ForeignKey(
        Stable,
        on_delete=models.RESTRICT
    )
    retirement_date = models.DateField(default=None, blank=True, null=True)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tournament(models.Model):
    TOKYO, OSAKA, NAGOYA, FUKUOKA = "HBASHO_TOKYO", "HBASHO_OSAKA", "HBASHO_NAGOYA", "HBASHO_FUKUOKA"
    TOURNAMENT_LOCATIONS = (
        (TOKYO, "Tokyo"),
        (OSAKA, "Osaka"),
        (NAGOYA, "Nagoya"),
        (FUKUOKA, "Fukuoka")
    )
    location = models.IntegerField(choices=TOURNAMENT_LOCATIONS, default=TOKYO)
    start_date = models.DateField()
    end_date = models.DateField()
    champion = models.ForeignKey(
        Wrestler,
        on_delete=models.RESTRICT,
        null=True
    )
    wrestler = models.ManyToManyField(Wrestler, through='TournamentWrestler')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_tournament_location_label(self):
        return TournamentLocations(self.location).name.title()

class Rank(models.Model):
    MAKUUCHI, JURYO = "HBASHO_MAKUUCHI", "HBASHO_JURYO"
    DIVISION_CHOICES = (
        (MAKUUCHI, "Makuuchi"),
        (JURYO, "Juryo"),
    )
    order_by = models.IntegerField()
    title = models.CharField(max_length=128)
    division = models.CharField(choices=DIVISION_CHOICES)

class TournamentWrestler(models.Model):
    wrestler = models.ForeignKey(Wrestler, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.RESTRICT)
    withdrew = models.BooleanField(default=False)
    shukun_prize = models.BooleanField(default=False)
    kanto_prize = models.BooleanField(default=False)
    gino_prize = models.BooleanField(default=False)

