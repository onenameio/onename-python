# -*- coding: utf-8 -*-
"""
    API Client
    ~~~~~
    :copyright: (c) 2015 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

import json
import requests

requests.packages.urllib3.disable_warnings()

BASE_URL = "https://api.onename.com/v1"

class OnenameClient:
    def __init__(self, api_id, api_secret, base_url=BASE_URL):
        self.api_id = api_id
        self.api_secret = api_secret
        self.base_url = base_url

    def _get_request(self, url):
        response = requests.get(
            url, auth=(self.api_id, self.api_secret), verify=False)
        return json.loads(response.text)

    def _post_request(self, url, payload):
        headers = {'content-type': 'application/json'}
        response = requests.post(
            url, data=json.dumps(payload), auth=(self.api_id, self.api_secret),
            headers=headers, verify=False)
        return json.loads(response.text)

    def get_user(self, username):
        url = self.base_url + "/users/" + username
        return self._get_request(url)

    def get_users(self, usernames):
        url = self.base_url + "/users/" + ','.join(usernames)
        return self._get_request(url)

    def get_all_users(self):
        url = self.base_url + "/users"
        return self._get_request(url)

    def search_users(self, query):
        url = self.base_url + "/search?query=" + query
        return self._get_request(url)

    def get_user_stats(self):
        url = self.base_url + "/stats/users"
        return self._get_request(url)

    def get_address_info(self, address):
        url = self.base_url + "/addresses/" + address
        return self._get_request(url)

    def register_user(self, username, address):
        payload = {
            'pasname': username,
            'recipient_address': address
        }
        url = self.base_url + "/users"
        return self._post_request(url, payload)

    def broadcast_transaction(self, payload):
        url = self.base_url + "/transactions"
        return self._post_request(url, payload)

    def get_dkim_info(self, domain):
        url = self.base_url + "/domains/" + domain + "/dkim"
        return self._get_request(url)
