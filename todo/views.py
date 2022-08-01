""" takes care of communication between the frontend and the backend """
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    """ Provides a means to editing existing items """
    # This method will either return the item if it exists
    #  or a 404 page not found if not.
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        # Difference between add and edit is that's we must give
        # our form the specific item instance we want to update.
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """ Provides a means to toggling items done to not done and viceversa """
    # This method will either return the item if it exists
    #  or a 404 page not found if not.
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    """ Provides a means to deleting items """
    # This method will either return the item if it exists
    #  or a 404 page not found if not.
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
