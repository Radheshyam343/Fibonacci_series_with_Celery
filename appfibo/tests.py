from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class FibonacciTestCase(TestCase):
    def test_fibonacci_endpoint(self):
        # test POST request with n = 10
        response = self.client.post(reverse('fibonacci'), data={'key': '10'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['nth'], '55')

        # test POST request with invalid input
        response = self.client.post(reverse('fibonacci'), data={'key': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'], 'error')
