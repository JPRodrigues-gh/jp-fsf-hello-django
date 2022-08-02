""" Views test py-file """

from django.test import TestCase
# import the Item model so we can do crud operations in Django tests
from .models import Item

# Create your tests here.
class TestView(TestCase):
    """  class inherits Testcase and contains all the tests on the views """

    def test_get_todo_list(self):
        """ test that we can get the todo list which is the home page """

        # To test the HTTP responses of the views we can use a built-in HTTP
        #  client that comes with the Django testing framework

        # get the home page - providing the URL slash will get the home page
        response = self.client.get('/')
        # confirm that the response.status code is equal to 200,
        #  a successful HTTP response
        self.assertEqual(response.status_code, 200)
        # confirm the view uses the correct template and tell
        #  it the template we expect it to use in the response
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """ test that we can get the add_item page """

        # To test the HTTP responses of the views we can use a built-in HTTP
        #  client that comes with the Django testing framework

        # get the add_item page providing the URL
        response = self.client.get('/add')
        # confirm that the response.status code is equal to 200,
        #  a successful HTTP response
        self.assertEqual(response.status_code, 200)
        # confirm the view uses the correct template and tell
        #  it the template we expect it to use in the response
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """ test that we can get the edit_item page """

        # To test the HTTP responses of the views we can use a built-in HTTP
        #  client that comes with the Django testing framework

        # create an item to use in this test
        item = Item.objects.create(name='Item for edit_item page test')
        # get the edit_item page providing the URL and
        #  the id of the item added/created above
        response = self.client.get(f'/edit/{item.id}')
        # confirm that the response.status code is equal to 200,
        #  a successful HTTP response
        self.assertEqual(response.status_code, 200)
        # confirm the view uses the correct template and tell
        #  it the template we expect it to use in the response
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ test that we can add an item """

        # simulate submitting the item form with new item
        response = self.client.post('/add', {'name': 'Test adding new item'})
        # If the item is added successfully the view should redirect
        #  back to the home page. Use assertRedirects to confirm
        #  that it redirects back to slash.
        self.assertRedirects(response, '/')
        # # get new item from the database passing it the item.id
        # added_item = response.objects.get(id=item.id)
        # # verify that the item was updated
        # self.assertEqual(added_item.name, 'Test adding new item')

    def test_can_edit_item(self):
        """ test that we can edit an item """

        # To test the HTTP responses of the views we can use a built-in HTTP
        #  client that comes with the Django testing framework

        # create an item to use in this test
        item = Item.objects.create(name='Test editing an item')
        # get the edit_item page providing the URL and
        #  the id of the item added/created above
        response = self.client.post(f'/edit/{item.id}', {'name': 'Edited name'})
        # If the item is added successfully the view should redirect
        #  back to the home page. Use assertRedirects to confirm
        #  that it redirects back to slash.
        self.assertRedirects(response, '/')
        # get new item from the database passing it the item.id
        updated_item = Item.objects.get(id=item.id)
        # verify that the item was updated
        self.assertEqual(updated_item.name, 'Edited name')

    def test_can_delete_item(self):
        """ test that we can delete an item """

         # create an item to use in this test
        item = Item.objects.create(name='Item for delete test')
        # get the delete page providing the URL and
        #  the id of the item added/created above
        response = self.client.get(f'/delete/{item.id}')
        # If the item is deleted successfully the view should redirect
        #  back to the home page. Use assertRedirects to confirm
        #  that it redirects back to slash.
        self.assertRedirects(response, '/')
        # to prove that the item is in fact deleted, try to get it from the
        #  database using .filter and passing it the item.id
        existing_items = Item.objects.filter(id=item.id)
        # verify the view works by asserting whether the
        #  length of existing_items is zero
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_done(self):
        """ test that we can toggle done checkbox """

         # create an item to use in this test with done set to True
        item = Item.objects.create(name='Item for toggle test', done=True)
        # get the toggle page providing the URL and
        #  the id of the item added/created above
        response = self.client.get(f'/toggle/{item.id}')
        # If the item is deleted successfully the view should redirect
        #  back to the home page. Use assertRedirects to confirm
        #  that it redirects back to slash.
        self.assertRedirects(response, '/')
        # get new item from the database passing it the item.id
        updated_item = Item.objects.get(id=item.id)
        # check the item's done status
        self.assertFalse(updated_item.done)
