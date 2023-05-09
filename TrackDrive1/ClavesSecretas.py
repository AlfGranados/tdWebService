import secrets
from django.core.management.utils import get_random_secret_key

secret_key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(92))

print(secret_key)
print(get_random_secret_key())

SECRET_KEY = 'django-insecure-tv5fzd3_30threrj6^5&#l!gbd%w+gtrfunhsf-g&6_99v3=@8'

print("La longitud de la clave secreta es", len(SECRET_KEY))
