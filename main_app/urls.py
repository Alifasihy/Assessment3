from django.urls import path
from . import views

urlpatterns = [
    path('', views.widget_home, name='home'),
]