from django.db import models


DIVISION_CHOICES = (
    (MAKUUCHI := "HBASHO_MAKUUCHI", "Makuuchi"),
    (JURYO := "HBASHO_JURYO", "Juryo"),
)


class Stable(models.Model):
    name = models.CharField(max_length=32, unique=True)
    name_kanji = models.CharField(max_length=32, unique=True)
    location = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class Wrestler(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    first_name_kanji = models.CharField(max_length=32)
    last_name_kanji = models.CharField(max_length=32)
    height_cm = models.DecimalField(max_digits=5, decimal_places=1)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=1)
    stable = models.ForeignKey(
        Stable,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    retirement_date = models.DateField(default=None, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["last_name", "first_name"],
                name="unique_wrestler_name",
            ),
            models.UniqueConstraint(
                fields=["last_name_kanji", "first_name_kanji"],
                name="unique_wrestler_name_kanji",
            ),
        ]


class Tournament(models.Model):
    TOURNAMENT_LOCATIONS = (
        (TOKYO := "HBASHO_TOKYO", "Tokyo"),
        (OSAKA := "HBASHO_OSAKA", "Osaka"),
        (NAGOYA := "HBASHO_NAGOYA", "Nagoya"),
        (FUKUOKA := "HBASHO_FUKUOKA", "Fukuoka"),
    )
    location = models.CharField(max_length=128, choices=TOURNAMENT_LOCATIONS, default=TOKYO)
    start_date = models.DateField()
    end_date = models.DateField()
    wrestlers = models.ManyToManyField(Wrestler, through="TournamentWrestler")
    champion = models.ForeignKey(
        Wrestler,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        related_name="champion",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        month = self.start_date.strftime("%b")
        year = self.start_date.year
        return f"{month} {year}"


class Rank(models.Model):
    order_by = models.IntegerField()
    title = models.CharField(max_length=128, unique=True)
    division = models.CharField(max_length=128, choices=DIVISION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order_by']


class TournamentWrestler(models.Model):
    wrestler = models.ForeignKey(
        Wrestler,
        on_delete=models.CASCADE,
    )
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.RESTRICT)
    withdrew = models.BooleanField(default=False)
    shukun_prize = models.BooleanField(default=False)
    kanto_prize = models.BooleanField(default=False)
    gino_prize = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wrestler

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["wrestler", "tournament"],
                name="unique_tournament_wrestler",
            )
        ]


class Match(models.Model):
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    wrestler_west = models.ForeignKey(
        Wrestler,
        on_delete=models.RESTRICT,
        related_name="wrestler_west",
    )
    wrestler_east = models.ForeignKey(
        Wrestler,
        on_delete=models.RESTRICT,
        related_name="wrestler_east",
    )
    winner = models.ForeignKey(
        Wrestler,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        related_name="winner",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_day_number(self):
        return (self.date - self.tournament.start_date).days + 1

    def __str__(self):
        return f"Day {self.get_day_number()}: {self.wrestler_east} vs. {self.wrestler_west}"


class WrestlerRecord(models.Model):
    wrestler = models.OneToOneField(
        Wrestler,
        on_delete=models.CASCADE,
        primary_key=True
    )
    wins = models.IntegerField(default=0)
    lossess = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    championships_makuuchi = models.IntegerField(default=0)
    kinboshi = models.IntegerField(default=0)
    shukun_prizes = models.IntegerField(default=0)
    kanto_prizes = models.IntegerField(default=0)
    gino_prizes = models.IntegerField(default=0)
    highest_rank = models.ForeignKey(
        Rank,
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wrestler
