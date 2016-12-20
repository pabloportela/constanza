import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_contacts(self):
        # Issue a GET request.
        response = self.client.get('/contacts/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered json contains 4 contacts.
        self.assertEqual(len(response.json()), 4)
