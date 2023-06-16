from django.urls import path
from tasks.views import show_tasks, delete, mark_completed

urlpatterns = [
    path("", show_tasks, name="show_tasks"),
    path("delete/<int:id>", delete, name="delete"),
    path("mark_completed/<int:id>", mark_completed, name="mark_completed"),
]
