import unittest
from fastapi.testclient import TestClient
from main import app  

class TestBillingApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_record_call(self):
        response = self.client.post('/mobile/{call_record.username}/call', json={'call_duration': 60, "username": "testuser"})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], 'Call recorded successfully')
        self.assertEqual(data['block_count'], 2)  

    def test_get_billing_info(self):
        response = self.client.get('/mobile/testuser/billing/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('call_count', data)
        self.assertIn('block_count', data)

if __name__ == '__main__':
    unittest.main()
