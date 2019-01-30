from .. import models
from django.test import TestCase
from django.shortcuts import resolve_url
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_jwt.utils import jwt_decode_handler
from time import sleep


class JWTTests(TestCase):
    def setUp(self):
        self.username = 'test'
        self.password = 'testit!'

        self.user = models.User.objects.create_user(
            username=self.username,
            password=self.password,
            email='testit@example.com',
        )

    def test_obtain(self):
        client = APIClient(enforce_csrf_checks=True)
        response = client.post(
            path=resolve_url('jwt_obtain'),
            data=dict(
                username=self.username,
                password=self.password,
            ),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        decoded_payload = jwt_decode_handler(response.data['token'])
        self.assertEqual(decoded_payload['username'], self.username)

    def test_obtain_wrong(self):
        client = APIClient(enforce_csrf_checks=True)
        response = client.post(
            path=resolve_url('jwt_obtain'),
            data=dict(
                username=self.username,
                password='wrong',
            ),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh(self):
        client = APIClient(enforce_csrf_checks=True)
        response = client.post(
            path=resolve_url('jwt_obtain'),
            data=dict(
                username=self.username,
                password=self.password,
            ),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        orig_token = response.data['token']

        sleep(1)
        response = client.post(
            path=resolve_url('jwt_refresh'),
            data=dict(token=orig_token),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_token = response.data['token']

        self.assertNotEqual(orig_token, new_token)
        self.assertEqual(
            jwt_decode_handler(orig_token)['orig_iat'],
            jwt_decode_handler(new_token)['orig_iat'],
        )
        self.assertLess(
            jwt_decode_handler(orig_token)['exp'],
            jwt_decode_handler(new_token)['exp'],
        )
