from django.apps import AppConfig


class ForumConfig(AppConfig):
    """Registers the forum as a Django app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
