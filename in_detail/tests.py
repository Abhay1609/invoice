from django.test import TestCase

# Create your tests here.
# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):

        self.client = APIClient()
        self.invoice_data = {
            'date': '2005-05-12',
            'invoice_no': '121',
            'customer_name': 'Abhay Pratap',
            'invoice_details': [
                {

                    'description': "Polish",
                    "quantity": 1,
                    "unit_price": "165.00",
                    "price": "10.00",

                }
            ]
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# You can add more test cases for other endpoints and scenarios





