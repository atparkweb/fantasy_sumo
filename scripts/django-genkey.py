from django.core.management.utils import get_random_secret_key

print(f'Here is your SECRET_KEY: {get_random_secret_key()}')
