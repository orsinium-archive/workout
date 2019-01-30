# external
from django.test import TestCase
from rest_framework import status

# app
from .mixins import JWTMixin


class DayTests(JWTMixin, TestCase):
    def test_list(self):
        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        # add exercise
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exercise_id = response.data['id']

        # add day
        response = self.client.post('/api/v1/days/', data=dict(
            name='feet',
            exercises=[exercise_id],
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'feet')

    def test_detail(self):
        # add exercise
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exercise_id = response.data['id']

        # add day
        response = self.client.post('/api/v1/days/', data=dict(
            name='feet',
            exercises=[exercise_id],
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get info
        day_id = response.data['id']
        response = self.client.get('/api/v1/days/{}/'.format(day_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'feet')
        self.assertEqual(response.data['exercises'], [exercise_id])

    def test_add(self):
        # add exercise
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exercise_id = response.data['id']

        # check list
        response = self.client.get('/api/v1/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # add day
        response = self.client.post('/api/v1/days/', data=dict(
            name='feet',
            exercises=[exercise_id],
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete(self):
        # add exercise
        response = self.client.post('/api/v1/exercises/', data=dict(name='running'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exercise_id = response.data['id']

        # add day
        response = self.client.post('/api/v1/days/', data=dict(
            name='feet',
            exercises=[exercise_id],
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # delete
        day_id = response.data[0]['id']
        response = self.client.delete('/api/v1/days/{}/'.format(day_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
