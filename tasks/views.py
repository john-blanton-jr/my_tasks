from django.shortcuts import render


def show_tasks(request):

    return render(request, "tasks/tasks.html")
