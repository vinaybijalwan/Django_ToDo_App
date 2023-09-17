from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo



# Create your views here.

def homepageNew(request):
    todos = ToDo.objects.all()
    if request.method == "POST":
        post = ToDo()
        post.title = request.POST['title']
        post.save()
        
        return redirect('homeNew')
    context = {
            'todos': todos,
             }
        
    return render(request, 'base/home.html', context)
    



def delete_todo(request, todo_id):
    # Fetch the to-do item to delete using get_object_or_404
    todo = get_object_or_404(ToDo, pk=todo_id)

    if request.method == 'POST':
        # Delete the to-do item
        todo.delete()

    # Redirect back to the homepage or any other desired page
    return redirect('homeNew')


def edit_todo(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)

    if request.method == 'POST':
        edited_title = request.POST['edited_title']
        todo.title = edited_title
        todo.save()

    return redirect('homeNew')
