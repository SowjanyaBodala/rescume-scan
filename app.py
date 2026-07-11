import os
from django.core.wsgi import get_wsgi_application

# Set default settings module for Render
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resumescreener.settings')

# Expose WSGI application as 'app' for gunicorn app:app
app = get_wsgi_application()
