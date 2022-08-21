from enum import IntEnum

class TournamentLocations(IntEnum):
    TOKYO = 1
    OSAKA = 2
    NAGOYA = 3
    FUKUOKA = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
