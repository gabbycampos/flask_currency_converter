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
            #import pdb
            #pdb.set_trace()

            res = self.client.get('/')
            html = res.get_data(as_text=True) # returning text

            self.assertEqual(res.status_code, 200)
            self.assertIn('Converting to', html)
            self.assertIn('Amount', html)
            self.assertIn('Converting from', html)

    def test_convert(self):
        """ Test convertion """
        with self.client:
            res = self.client.post('/convert', data={'from': 'USD', 'to': 'USD', 'amount': '1'})

            self.assertEqual(res.status_code, 302)
            self.assertEqual(session['result'], 1)
            self.assertEqual(session['symbol'], 'US$')

    def test_result(self):
        """ Test result display """
        with self.client:
            with self.client.session_transaction() as sess:
                sess['result'] = 1
                sess['symbol'] = '$'

            res = self.client.get('/result')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('$ 1', html)

    def test_error(self):
        with self.client:
            """ Test error """
            with self.client.session_transaction() as sess:
                sess['msg'] = 'This amount is not valid'
                #sess['sym'] = 'Not a valid currency code: ' # FAILED
            
            res = self.client.get('/error')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('This amount is not valid', html)
            #self.assertIn('Not a valid currency code: ', html)

