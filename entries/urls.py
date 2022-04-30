from django.urls import path
from .views import (
    EntryCreateView,
    EntryListView,
    EntryDeleteView,
    EntryUpdateView,
    EntryDetailView,
    TagListView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("tags/<slug:tag_slug>/", TagListView.as_view(), name="posts_by_tags"),
    path("new-entry", login_required(EntryCreateView.as_view()), name="new-entry"),
    path("", login_required(EntryListView.as_view()), name="list-entries"),
    path("update-entry/<int:pk>",
         login_required(EntryUpdateView.as_view()), name="update-entry"),
    path("delete-entry/<int:pk>", EntryDeleteView, name="delete-entry"),
    path("entry/<int:pk>", EntryDetailView, name="detail-entry"),
]
