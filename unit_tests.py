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

class GetUsersTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_users(self):
        test_username = TEST_USERS[0]['username']
        users = onename_client.get_users([test_username])
        self.assertTrue(test_username in users)
        user = users[test_username]
        self.assertTrue('profile' in user)
        user_profile = user['profile']
        self.assertTrue(user_profile['website'] == TEST_USERS[0]['website'])

def test_main():
    test_support.run_unittest(
        GetUsersTest
    )

if __name__ == '__main__':
    test_main()
