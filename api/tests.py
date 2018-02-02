from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from .models import NPO, User, Opportunity


class NPOAPITests(APITestCase):

    # With fixture
    fixtures = ['one_npo.json']

    # Without fixture
    '''
    def setUp(self):
        user = User.objects.create(email='user@example.com', first_name='Al',
                                   last_name='User')
        NPO.objects.create(organization_name='Test Organization',
                           org_short_name='TestOrg', admin_user=user)
        user.set_password('testexample')
        user.save()
        User.objects.create(email='user2@example.com', first_name='El',
                            last_name='User')
    '''

    def test_list_npos(self):
        response = self.client.get('/npos/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        npo = response.data[0]
        self.assertEqual(npo['organization_name'], 'Test Organization')
        self.assertEqual(npo['admin_user'], 1)
        self.assertEqual(len(npo['employees']), 0)

        self.assertContains(response, 'Test Organization')

    def test_create_npo(self):
        payload = {
            'organization_name': 'Another Test Organization',
            'org_short_name': 'ATOrg',
        }

        response = self.client.post('/npos/', data=payload)
        # Need to log in, so response is currently 401
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.post('/npos/', data=payload)
        # Missing parameter, `admin_user`
        self.assertEqual(response.status_code, 400)

        payload['admin_user'] = 2
        payload['employees'] = [1]
        response = self.client.post('/npos/', data=payload)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(len(NPO.objects.all()), 2)

    def test_retrieve_npo(self):
        response = self.client.get('/npos/1/')

        self.assertEqual(response.status_code, 200)
        npo = response.data
        self.assertEqual(npo['organization_name'], 'Test Organization')

    def test_update_npo(self):
        response = self.client.get('/npos/1/')
        payload = response.data

        # First test PUT
        payload['organization_name'] = 'Renamed Organization'
        payload['employees'] = [2]
        response = self.client.put('/npos/1/', data=payload)
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.put('/npos/1/', data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['organization_name'],
                         'Renamed Organization')

        # Next test PATCH
        payload = {
            'organization_name': 'Test Organization',
        }

        response = self.client.patch('/npos/1/', data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['organization_name'],
                         'Test Organization')

    def test_delete_npo(self):
        response = self.client.delete('/npos/1/')
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.delete('/npos/1/')
        self.assertEqual(response.status_code, 204)

        self.assertFalse(NPO.objects.exists())


class OpportunityAPITests(APITestCase):

    # With fixture
    fixtures = ['one_npo.json']

    def test_list_opportunities(self):
        response = self.client.get('/opportunity/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        opportunity = response.data[0]
        self.assertEqual(opportunity['opportunity_name'], 'A great time for all!')

        self.assertContains(response, 'A great time')

    def test_create_opportunity(self):
        payload = {
            'organization': '1',
            'opportunity_name': 'Another great opportunity!',
        }

        response = self.client.post('/opportunity/', data=payload)
        # Need to log in, so response is currently 401
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.post('/opportunity/', data=payload)
        # Missing parameters
        self.assertEqual(response.status_code, 400)

        payload['start_date'] = '2018-02-19T03:40:57Z'
        payload['end_date'] = '2018-02-25T03:40:58Z'
        response = self.client.post('/opportunity/', data=payload)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(len(Opportunity.objects.all()), 2)

    def test_retrieve_opportunity(self):
        response = self.client.get('/opportunity/1/')

        self.assertEqual(response.status_code, 200)
        npo = response.data
        self.assertEqual(npo['opportunity_name'], 'A great time for all!')

    def test_update_opportunity(self):
        response = self.client.get('/opportunity/1/')
        payload = response.data

        # First test PUT
        payload['opportunity_name'] = 'Renamed opportunity'
        response = self.client.put('/opportunity/1/', data=payload)
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.put('/opportunity/1/', data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['opportunity_name'],
                         'Renamed opportunity')

        # Next test PATCH
        payload = {
            'opportunity_name': 'Test opportunity again',
        }

        response = self.client.patch('/opportunity/1/', data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['opportunity_name'],
                         'Test opportunity again')

    def test_delete_npo(self):
        response = self.client.delete('/opportunity/1/')
        self.assertEqual(response.status_code, 401)

        self.client.login(username='user@example.com', password='testexample')
        response = self.client.delete('/opportunity/1/')
        self.assertEqual(response.status_code, 204)

        self.assertFalse(Opportunity.objects.exists())
