from unittest import TestCase
from app import app
from flask import session

class ConvertTests(TestCase):
    """ Tests for the currency converter app """
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        """ Test to check that HTML is displayed """
        with self.client:
            import pdb
            pdb.set_trace()

            res = self.client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            # self.assertIn('<label>Converting to</label>', html)
            # self.assertIn('<label>Amount</label>', html)