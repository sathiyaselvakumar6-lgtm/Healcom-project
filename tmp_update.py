import os

path = 'healcom/settings.py'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

apps = [
    "    'django.contrib.sites',",
    "    'allauth',",
    "    'allauth.account',",
    "    'allauth.socialaccount',",
    "    'allauth.socialaccount.providers.google',"
]
c = c.replace("    'core',\n]", "    'core',\n" + "\n".join(apps) + "\n]\n\nSITE_ID = 1")

middlewares = [
    "    'allauth.account.middleware.AccountMiddleware',"
]
c = c.replace("    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]", "    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n" + "\n".join(middlewares) + "\n]")

extra_settings = """
# --- ALLAUTH OAUTH -----------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none' 
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}
"""
c = c.replace("EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'", "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'\n" + extra_settings)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Settings updated.')
