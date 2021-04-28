from django.apps import AppConfig


class MotivatorsConfig(AppConfig):
    name = 'books_module'

    def ready(self):
        import books_module.signals
