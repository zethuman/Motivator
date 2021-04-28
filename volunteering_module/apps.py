from django.apps import AppConfig


class VolunteeringModuleConfig(AppConfig):
    name = 'volunteering_module'

    def ready(self):
        import volunteering_module.signals
