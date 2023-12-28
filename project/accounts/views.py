from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):
    if request.user.is_superuser:
        notes = Note.objects.all()
    else:
        notes = Note.objects.filter(created_by=request.user)
    context = {
        'notes': notes
    }
    return render(request, "dashboard.html", context)

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            messages.success(request, "Note added successfully!")
            return redirect('dashboard')
    else:
        form = NoteForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context)

@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('dashboard')

@login_required
def update_note(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, "edit_note.html", context)
