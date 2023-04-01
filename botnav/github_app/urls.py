from django.urls import path
from botnav.github_app.views import CreateRepoAPIView, ReadRepoApiView

urlpatterns = [
    # C
    path("create/repository", view=CreateRepoAPIView.as_view(), name="create_repository"),
    # R
    path("read/repository", view=ReadRepoApiView.as_view(), name="reads_reporitory"),
    path("read/repositories", view=ReadRepoApiView.as_view(), name="read_repositorie"),
    # U
    # D
]
