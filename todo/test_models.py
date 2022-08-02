""" Views test py-file """

from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    """  class inherits Testcase and contains all the tests on the models """

    def test_done_defaults_to_false(self):
        """
        test that our todo items will be created by
         default with the done status of false
        """

        # create an item to use in this test
        item = Item.objects.create(name='Test Todo Item')
        # confirm that it's done status is in fact false by default
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """ tested the string method of our item model """

        # create an item to use in this test
        item = Item.objects.create(name='Test Todo Item')
        # confirm that this name is returned
        #  when we render this item as a string
        self.assertEqual(str(item), 'Test Todo Item')
