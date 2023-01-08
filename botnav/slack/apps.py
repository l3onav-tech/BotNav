from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "botnav.slack"
    verbose_name = _("Slack")

    def ready(self):
        try:
            import botnav.slack.signals  # noqa F401
        except ImportError:
            pass
