import os
import flaskr
import unittest

class APITestCase(unittest.TestCase):

    def setUp(self):
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()

    def tearDown(self):
        pass

    def test_calculate(self):
        resp = self.app.get('/calculate?x=1')
        assert 'undefined' in resp.data

if __name__ == '__main__':
    unittest.main()
