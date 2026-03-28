import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healcom.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

# 1. Ensure Site exists (already done but safe to repeat)
site, _ = Site.objects.get_or_create(id=1, defaults={'domain': '127.0.0.1:8000', 'name': 'Healcom'})

# 2. Create a Placeholder Social App for Google
# This prevents the "SocialApp DoesNotExist" crash when loading the login page.
app, created = SocialApp.objects.get_or_create(
    provider='google',
    name='Google Login',
    defaults={
        'client_id': 'PLACEHOLDER_CLIENT_ID',
        'secret': 'PLACEHOLDER_SECRET',
    }
)

# 3. Link the app to the site
if site not in app.sites.all():
    app.sites.add(site)
    app.save()

print(f"Placeholder SocialApp '{app.name}' for provider '{app.provider}' created and linked to Site ID {site.id}.")
print("The login page should now load correctly.")
