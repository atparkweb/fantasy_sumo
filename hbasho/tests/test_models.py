from django.test import TestCase
from .models import Wrestler

class Wrestler(TestCase):
    def create_wrestler(self, first_name="Test", last_name="Rikishi", first_name_kanji="検診", last_name_kanji="力士", height_cm=180.0, weight_kg=140.0):
        return Wrestler.objects.create(first_name=first_name, last_name=last_nam, first_name_kanji=first_name_kanji, last_name_kanji=last_name_kanji, height_cm=180.0, weight_kg=140.0)

    def test_wrestler_creation(self):
        wrestler = create_wrestler()
        self.assertTrue(isinstance(wrestler, Wrestler))
        self.assertEqual(w.__unicode__(), wrestler.first_name)
