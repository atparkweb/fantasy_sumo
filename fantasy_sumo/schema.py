import graphene
from graphene_django import DjangoObjectType

from hbasho.models import Wrestler, Stable

class WrestlerType(DjangoObjectType):
    class Meta:
        model = Wrestler
        fields = (
            "id",
            "first_name",
            "last_name",
            "first_name_kanji",
            "last_name_kanji",
            "height_cm",
            "weight_kg",
            "stable",
            "retirement_date",
            "birthdate",
            "birthplace",
        )

class StableType(DjangoObjectType):
    class Meta:
        model = Stable
        fields = (
            "id",
            "name",
            "name_kanji",
            "location",
            "wrestlers",
        )

class Query(graphene.ObjectType):
    all_wrestlers = graphene.List(WrestlerType)
    stable_by_name = graphene.Field(StableType, name=graphene.String(required=True))

    def resolve_all_wrestlers(root, info):
        return Wrestler.objects.select_related("stable").all()

    def resolve_stable_by_name(root, info, name):
        try:
            return Stable.objects.get(name=name)
        except Stable.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
