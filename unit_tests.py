import json
import traceback
import unittest
from test import test_support

from onename import OnenameClient
from settings import ONENAME_API_ID, ONENAME_API_SECRET

onename_client = OnenameClient(ONENAME_API_ID, ONENAME_API_SECRET)

TEST_USERS = [
    {'username': 'albertwenger', 'website': 'http://continuations.com'}
]

class BasicAPITest(unittest.TestCase):
    def setUp(self):
        self.test_user = TEST_USERS[0]
        self.test_query = 'wenger'

    def tearDown(self):
        pass

    def test_get_users(self):
        users = onename_client.get_users([self.test_user['username']])
        self.assertTrue(self.test_user['username'] in users)
        user = users[self.test_user['username']]
        self.assertTrue('profile' in user)
        self.assertTrue(user['profile']['website'] == self.test_user['website'])

    def test_search_users(self):
        resp = onename_client.search_users('wenger')
        self.assertTrue('results' in resp)
        self.assertTrue(len(resp['results']) > 0)

    def test_get_user_stats(self):
        resp = onename_client.get_user_stats()
        self.assertTrue('stats' in resp)
        self.assertTrue('registrations' in resp['stats'])

    def test_get_unspents(self):
        resp = onename_client.get_unspents('N8PcBQnL4oMuM6aLsQow6iG59yks1AtQX4')
        self.assertTrue('unspents' in resp)

    def test_get_names_owned(self):
        resp = onename_client.get_names('MyVZe4nwF45jeooXw2v1VtXyNCPczbL2EE')
        self.assertTrue('names' in resp)

    def test_get_dkim_info(self):
        resp = onename_client.get_dkim_info('onename.com')
        self.assertTrue('public_key' in resp and 'key_type' in resp)


def test_main():
    test_support.run_unittest(
        BasicAPITest
    )

if __name__ == '__main__':
    test_main()
