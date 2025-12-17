from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("note-list/", views.Note_list.as_view(), name="list"),
    path("note-create/", views.Note_create.as_view(), name="create"),
    path("<int:pk>/note-edit/", views.Note_edit.as_view(), name="edit"),
    path("<int:pk>/note-detail/", views.Note_detail.as_view(), name="detail"),
    path("<int:pk>/delete/", views.Notedelete.as_view(), name="delete"),
    path("search/", views.Notesearch.as_view(), name="search"),
]
