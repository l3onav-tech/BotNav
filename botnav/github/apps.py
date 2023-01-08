from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Githubonfig(AppConfig):
    name = "botnav.github"
    verbose_name = _("Github")

    def ready(self):
        try:
            import botnav.github.signals  # noqa F401
        except ImportError:
            pass
