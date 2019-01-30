# external
from django.test import TestCase
from rest_framework import status

# app
from .mixins import JWTMixin


class PlanTests(JWTMixin, TestCase):
    def test_smoke(self):
        # check list
        response = self.client.get('/api/v1/plans/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

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
        day_id = response.data['id']

        # check list
        response = self.client.get('/api/v1/days/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'feet')

        # add plan
        response = self.client.post('/api/v1/plans/', data=dict(
            name='main',
            days=[day_id],
        ))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        plan_id = response.data['id']

        # get info
        response = self.client.get('/api/v1/plans/{}/'.format(plan_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'main')
        self.assertEqual(response.data['days'], [day_id])

        # check list
        response = self.client.get('/api/v1/plans/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'main')

        # delete
        day_id = response.data[0]['id']
        response = self.client.delete('/api/v1/plans/{}/'.format(plan_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check list
        response = self.client.get('/api/v1/plans/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
