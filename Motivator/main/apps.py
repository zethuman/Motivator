from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals
