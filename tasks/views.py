from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required


def show_home(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "tasks/home.html", context)


@login_required
def show_tasks(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(False)
            form.owner = request.user
            form.save()
            return redirect("show_tasks")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }

    tasks = Task.objects.filter(owner=request.user)
    context = {
        "tasks": tasks,
        "form": form
    }
    return render(request, "tasks/tasks.html", context)


@login_required
def delete(request, id):
    item = Task.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('show_tasks'))


@login_required
def mark_completed(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse('show_tasks'))


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")
    else:
        form = TaskForm(instance=task)
    context = {
        "apply": task,
        "form": form,
    }
    return render(request, "tasks/edit.html", context)
