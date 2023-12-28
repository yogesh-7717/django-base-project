from django.contrib import admin
from .models import *
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ['id', 'title', 'note', 'created_by', 'created_at' ] 

admin.site.register(Note, NoteAdmin)