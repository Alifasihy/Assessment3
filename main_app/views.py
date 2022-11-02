from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import DeleteView, DetailView, CreateView


def widget_home(request):
    widget_list = Widget.objects.get()
    context = {
        'widget_list': widget_list
    }
    return render(request, 'index.html',context)