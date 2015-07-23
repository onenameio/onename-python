# -*- coding: utf-8 -*-
"""
    API Client
    ~~~~~
    :copyright: (c) 2015 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import json
import requests

from .config import ONENAME_API_ID, ONENAME_API_SECRET


class Client:

    def __init__(self, api_id=ONENAME_API_ID, api_secret=ONENAME_API_SECRET):

        self.api_id = api_id
        self.api_secret = api_secret
        self.base_url = "https://api.onename.com/v1"

    def _get_request(self, url):

        response = requests.get(url, auth=(self.api_id, self.api_secret),
                                verify=False)

        return json.loads(response.text)

    def _post_request(self, url, payload):

        response = requests.post(url, data=payload,
                                 auth=(self.api_id, self.api_secret),
                                 verify=False)

        return json.loads(response.text)

    def get_user(self, username):

        url = self.base_url + "/users/" + username

        return self._get_request(url)

    def get_search(self, query):

        url = self.base_url + "/search?query=" + query

        return self._get_request(url)

    def get_stats(self):

        url = self.base_url + "/users"

        return self._get_request(url)

    def get_address(self, address):

        url = self.base_url + "/addresses/" + address

        return self._get_request(url)

    def register_user(self, payload):

        url = self.base_url + "/users"

        return self._post_request(url, payload)

    def broadcast_transaction(self, payload):

        url = self.base_url + "/transactions"

        return self._post_request(url, payload)
