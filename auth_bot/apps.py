from django.apps import AppConfig


class AuthBotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_bot"

    def ready(self):
        import auth_bot.signals
