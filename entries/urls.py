from django.urls import path, include, re_path
from .views import (
    EntryCreateView,
    EntryListView,
    EntryDeleteView,
    EntryUpdateView,
    EntryDetailView,
)

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path("new-entry", EntryCreateView.as_view(), name="new-entry"),
    path("", EntryListView.as_view(), name="list-entries"),
    path("delete-entry/<int:pk>", EntryDeleteView, name="delete-entry"),
    path("update-entry/<int:pk>", EntryUpdateView.as_view(), name="update-entry"),
    path("entry/<int:pk>", EntryDetailView, name="detail-entry"),
]
