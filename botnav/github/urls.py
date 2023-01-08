from django.urls import path

from botnav.github.views import CreateRepositoryView

urlpatterns = [
    path("create/repository/", view=CreateRepositoryView.as_view(), name="create_repository"),
]
