from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Githubonfig(AppConfig):
    name = "botnav.github_app"
    verbose_name = _("Github_App")

    def ready(self):
        try:
            import botnav.github_app.signals  # noqa F401
        except ImportError:
            pass
