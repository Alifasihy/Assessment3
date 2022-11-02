from django import forms
from django.forms import ModelForm
from main_app.models import Widget

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = '__all__'