"""
create forms directly from the model itself and
allow Django to handle all the form validation
"""
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    ItemForm inherits all the functionality of forms.ModelForm
    """
    class Meta:
        """
        Provide inner class Meta to tell the form
         which model it's going to be associated with.
        This inner class just gives our form some information
         about itself, like which fields it should render,
         how it should display error messages and so on
        """
        model = Item
        fields = ['name', 'done']
