# external
from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

# app
from .. import models


class JWTMixin:
    def setUp(self):
        self.username = 'test'
        self.password = 'testit!'

        self.user = models.User.objects.create_user(
            username=self.username,
            password=self.password,
            email='testit@example.com',
        )
        self.client = self._get_client()

    def _get_client(self):
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

        client.credentials(HTTP_AUTHORIZATION="{0} {1}".format(
            api_settings.JWT_AUTH_HEADER_PREFIX,
            response.data['token'],
        ))
        return client
