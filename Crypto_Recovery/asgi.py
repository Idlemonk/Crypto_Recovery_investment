import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crypto_Recovery.settings')

from django.core.asgi import get_asgi_application

# Get Django's ASGI application
django_app = get_asgi_application()

