from django.urls import path

from .views import (
    SharedFileListCreateAPIView,
    SharedFileDetailAPIView,
    PeerListCreateAPIView,
    PeerDetailAPIView,
)


urlpatterns = [
    path(
        "shared-files/",
        SharedFileListCreateAPIView.as_view(),
        name="shared-file-list-create",
    ),
    path(
        "shared-files/<uuid:pk>/",
        SharedFileDetailAPIView.as_view(),
        name="shared-file-detail",
    ),
    path("peers/", PeerListCreateAPIView.as_view(), name="peer-list-create"),
    path("peers/<uuid:pk>/", PeerDetailAPIView.as_view(), name="peer-detail"),
]
