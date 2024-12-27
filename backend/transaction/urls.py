from django.urls import path
from . import views

urlpatterns = [
    path("files/", views.SharedFileListView.as_view(), name="shared-file-list"),
    path(
        "files/<uuid:pk>/",
        views.SharedFileDetailView.as_view(),
        name="shared-file-detail",
    ),
    path(
        "all-files/", views.AllSharedFileListView.as_view(), name="all-shared-file-list"
    ),
    path("peers/register/", views.PeerRegistrationView.as_view(), name="peer-register"),
    path("peers/<uuid:pk>/", views.PeerDetailView.as_view(), name="peer-detail"),
    path("peers/", views.PeerListView.as_view(), name="peer-list"),
]
