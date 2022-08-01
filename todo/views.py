""" takes care of communication between the frontend and the backend """
from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def get_todo_list(request):
    """
    ensure complete communication between the users of our app
     on the frontend and our database on the back end
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)

def add_item(request):
    """Provide a means for users to add items"""
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
