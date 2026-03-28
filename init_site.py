import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healcom.settings')
django.setup()

from django.contrib.sites.models import Site

# Initialize the default site for allauth
site, created = Site.objects.get_or_create(
    id=1,
    defaults={
        'domain': '127.0.0.1:8000',
        'name': 'Healcom Local'
    }
)

if not created:
    site.domain = '127.0.0.1:8000'
    site.name = 'Healcom Local'
    site.save()

print(f"Site configured: {site.domain}")
