from django.urls import path
from tasks.views import show_tasks, delete, mark_completed, show_home, edit_task

urlpatterns = [
    path("tasks/", show_tasks, name="show_tasks"),
    path("", show_home, name="show_home"),
    path("delete/<int:id>", delete, name="delete"),
    path("edit/<int:id>", edit_task, name="edit_task"),
    path("mark_completed/<int:id>", mark_completed, name="mark_completed"),
]
