from django.urls import path
from tasks.views import show_tasks, delete

urlpatterns = [
    path("", show_tasks, name="show_tasks"),
    path("delete/<int:id>", delete, name="delete"),
]
