""" Views test py-file """

from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    """  class inherits Testcase and contains all the tests on the models """

    def test_done_defaults_to_false(self):

        # create an item to use in this test
        item = Item.objects.create(name='Test Todo Item')
        # confirm that it's done status is in fact false by default
        self.assertFalse(item.done)
