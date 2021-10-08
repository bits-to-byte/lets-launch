from django.test import TestCase

# Create your tests here.
from models.customer import Customer

class CustomerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(first_name="Test", last_name="Customer",phone="1234567890")

    def test_first_name_label(self):
        author = Customer.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Customer.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_phone_label(self):
        author = Customer.objects.get(id=1)
        field_label = author._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_first_name_max_length(self):
        author = Customer.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

