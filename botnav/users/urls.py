from django.urls import path

from botnav.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
