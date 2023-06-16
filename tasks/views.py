from django.shortcuts import render
from tasks.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def show_tasks(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "tasks/tasks.html", context)


def delete(request, id):
    item = Task.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('show_tasks'))
