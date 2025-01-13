import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApiConfig(AppConfig):
    name = "mypet.api"
    verbose_name = _("Api")

    def ready(self):
        with contextlib.suppress(ImportError):
            import mypet.api.signals  # noqa: F401
