from django.test import TestCase
from django.urls import  reverse


class UsersTest(TestCase):
    def test_home_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
