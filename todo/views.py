""" takes care of communication between the frontend and the backend """
from django.shortcuts import render
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
