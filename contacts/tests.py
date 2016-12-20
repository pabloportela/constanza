import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    """Makes sure the app works with and only with the http GET method"""
    def setUp(self):
        self.client = Client()

    def test_get_contacts(self):
        # Issue a GET request.
        response = self.client.get('/contacts/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered json contains 4 contacts.
        self.assertEqual(len(response.json()), 4)

    def test_post_contacts(self):
        response = self.client.post('/contacts/')
        self.assertNotEqual(response.status_code, 200)

    def test_not_found(self):
        response = self.client.post('/i_do_not_exist/')
        self.assertEqual(response.status_code, 404)

