from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('add_note', views.add_note, name='add_note'),
    path('delete_note/<int:id>', views.delete_note, name='delete_note' ),
    path('update_note/<int:id>', views.update_note, name="update_note")
]
