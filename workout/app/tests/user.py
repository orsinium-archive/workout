from django.test import TestCase
from rest_framework import status
from .mixins import JWTMixin


class UserTests(JWTMixin, TestCase):
    def test_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # one user in database
        self.assertEqual(response.data[0]['id'], self.user.id)

    def test_detail(self):
        user_id = self.user.id
        response = self.client.get('/api/v1/users/{}/'.format(user_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.username)

    def test_add(self):
        response = self.client.post('/api/v1/users/', data=dict(
            username='lol',
            password='TestMeAgain',
            email='lol@example.com',
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
