from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


# Create your views here.

def homepage(request):
    todos = ToDo.objects.all()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a different page after saving the form
            return redirect('home')
    else:
        form = ToDoForm()
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'base/home.html', context)


