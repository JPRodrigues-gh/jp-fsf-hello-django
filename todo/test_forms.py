""" Forms test py-file """

from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """ class inherits Testcase and contains all the tests for this form """

    def test_item_name_is_required(self):
        """
        test to make sure that the name field
         is required in order to create an item
        """

        # instantiate a form without a name to simulate a user who submitted
        #  the form without filling it out. This form should be invalid.
        form = ItemForm({'name': ''})
        # use assertFalse, when the form is invalid it should also send
        #  back a dictionary of fields on which there were errors
        #  and the Associated error messages
        self.assertFalse(form.is_valid())
        # Knowing if the form is False we can be even more specific by using
        #  assertIn to assert whether or not there's a name key
        #  in the dictionary of form errors
        self.assertIn('name', form.errors.keys())
        # use assertEqual to check whether the error message on the name field
        #  is “this field is required.”, remember to include the period at the
        #  end, as the string will need to match exactly. Also just a note we
        #  are using the zero index here because the form will return a list
        #  of errors on each field and this verifies that the first item in
        #  that list is our string telling us the field is required.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """
        test to ensure the done field is not required. It shouldn't be
        since it has a default value of false on the item model.
        """

        # In this case we'll create the form sending only a name. And then
        # just test that the form is valid as it should be even without
        # selecting a done status.
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        assume that somewhere down the line another developer comes along and
        changes the item model, adding a field to it that contains some sort
        of information we don't want to display on the form. If you remember
        we actually defined the fields to display explicitly in the inner
        metaclass on the item form (forms.py). The reason for that is
        otherwise the form will display all fields on the model including
        those we might not want the user to see. That said this test is to
        ensure that the only fields that are displayed in the form are the
        name and done fields.
        """

        # For this test we can simply instantiate an empty form and then use
        #  assertEqual to check whether the form.meta.fields attribute is
        #  equal to a list with name and done in it. This will ensure that the
        #  fields are defined explicitly. If someone changes the item model
        #  down the road, our form won't accidentally display information we do
        #  not want it to. This will also protect against the fields being
        #  reordered, since the list must match exactly.
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
