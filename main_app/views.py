from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import DeleteView, DetailView, CreateView
from .forms import WidgetForm

def widget_home(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm
    context = {
        'widget_list': widget_list,
        'widget_form': widget_form
    }
    return render(request, 'index.html',context)

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id = widget_id).delete()
    return redirect('home')