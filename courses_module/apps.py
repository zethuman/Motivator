from django.apps import AppConfig


class CoursesModuleConfig(AppConfig):
    name = 'courses_module'

    def ready(self):
        import courses_module.signals
