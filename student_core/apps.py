from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class StudentCoreConfig(AppConfig):
    name = 'student_core'
    verbose_name = _('Student Core')

    def ready(self):
        import student_core.signals

# class StudentCoreConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'student_core'
