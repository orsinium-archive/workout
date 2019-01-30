# external
from django.test import TestCase
from rest_framework import status

# app
from .mixins import JWTMixin


class ExerciseTests(JWTMixin, TestCase):
    def test_list(self):
        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        # add
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'running')

    def test_detail(self):
        # add
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get info
        exercise_id = response.data['id']
        response = self.client.get('/api/v1/exercises/{}/'.format(exercise_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'running')

    def test_add(self):
        # add
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete(self):
        # add
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # delete
        exercise_id = response.data[0]['id']
        response = self.client.delete('/api/v1/exercises/{}/'.format(exercise_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
