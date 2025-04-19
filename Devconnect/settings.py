INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'profiles',
    'projects',
]

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
