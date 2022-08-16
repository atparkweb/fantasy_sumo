from django.db import models

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
