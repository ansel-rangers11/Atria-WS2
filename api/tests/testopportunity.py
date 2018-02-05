
from rest_framework.test import APITestCase

from api.models import User, Opportunity


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
