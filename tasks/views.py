# from django.shortcuts import render
from django.http import HttpResponse


def show_tasks(request):
    return HttpResponse("This view is working")
