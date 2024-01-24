from django.apps import AppConfig # need to include a few more necessary modules here!


class GeniricConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generic'


