from django.urls import path
from .views import (
    EntryCreateView,
    EntryListView,
    EntryDeleteView,
    EntryUpdateView,
    EntryDetailView,
)

urlpatterns = [
    path("new-entry", EntryCreateView.as_view(), name="new-entry"),
    path("", EntryListView.as_view(), name="list-entries"),
    path("delete-entry/<int:pk>", EntryDeleteView, name="delete-entry"),
    path("update-entry/<int:pk>", EntryUpdateView.as_view(), name="update-entry"),
    path("entry/<int:id>", EntryDetailView, name="detail-entry"),
]
