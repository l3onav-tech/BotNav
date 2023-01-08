from django.contrib import admin
from botnav.github.models import GithubModel
from django.utils.translation import gettext_lazy as _


@admin.register(GithubModel)
class UserAdmin(admin.ModelAdmin):
    pass
