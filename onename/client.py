# -*- coding: utf-8 -*-
"""
    API Client
    ~~~~~
    :copyright: (c) 2015-2016 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

import json
import requests

from pybitcoin import is_b58check_address
from pybitcoin import sign_all_unsigned_inputs

from registrar.crypto import get_pubkey_from_privkey

requests.packages.urllib3.disable_warnings()

BASE_URL = "https://api.onename.com/v1"


class OnenameClient:
    """
        Onename python API client
    """

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
        response = requests.post(url,
                                 data=json.dumps(payload),
                                 auth=(self.api_id, self.api_secret),
                                 headers=headers, verify=False)

        return json.loads(response.text)

    def get_users(self, usernames):

        if not isinstance(usernames, list):
            raise ValueError('"usernames" must be a list')
        url = self.base_url + "/users/" + ','.join(usernames)

        return self._get_request(url)

    def search_users(self, query):

        if not isinstance(query, (str, unicode)):
            raise ValueError('"query" must be a string')
        url = self.base_url + "/search?query=" + query

        return self._get_request(url)

    def register_user(self, username, address):

        if not isinstance(username, (str, unicode)):
            raise ValueError('"username" must be a string')

        if not is_b58check_address(address):
            raise ValueError('"address" must be a valid cryptocurrency address')

        url = self.base_url + "/users"

        payload = {
            'username': username,
            'recipient_address': address
        }

        return self._post_request(url, payload)

    def get_all_users(self):

        url = self.base_url + "/users"
        return self._get_request(url)

    def get_user_stats(self):

        url = self.base_url + "/stats/users"
        return self._get_request(url)

    def broadcast_transaction(self, signed_hex):

        url = self.base_url + "/transactions"
        payload = {
            'signed_hex': signed_hex
        }

        return self._post_request(url, payload)

    def get_unspents(self, address):

        if not is_b58check_address(address):
            raise ValueError('"address" must be a valid cryptocurrency address')
        url = self.base_url + "/addresses/" + address + "/unspents"

        return self._get_request(url)

    def get_names(self, address):

        if not is_b58check_address(address):
            raise ValueError('"address" must be a valid cryptocurrency address')
        url = self.base_url + "/addresses/" + address + "/names"

        return self._get_request(url)

    def get_dkim_info(self, domain):

        url = self.base_url + "/domains/" + domain + "/dkim"
        return self._get_request(url)

    def get_emails_token(self):

        url = self.base_url + "/emails"
        return self._get_request(url)

    def submit_email(self, email):

        url = self.base_url + "/emails"

        payload = {}
        data = self.get_emails_token()
        payload['token'] = data['token']
        payload['email'] = email

        return self._post_request(url, payload)

    def update_user(self, username, profile, owner_privkey):
        """
            Update profile_hash on blockchain
        """

        url = self.base_url + "/users/" + username + "/update"

        owner_pubkey = get_pubkey_from_privkey(owner_privkey)

        payload = {
            'profile': profile,
            'owner_pubkey': owner_pubkey
            }

        resp = self._post_request(url, payload)

        try:
            unsigned_tx = resp['unsigned_tx']
        except:
            return resp

        # sign all unsigned inputs
        signed_tx = sign_all_unsigned_inputs(owner_privkey, unsigned_tx_hex)

        return self.broadcast_transaction(signed_tx)

    def transfer_user(self, username, transfer_address, owner_privkey):
        """
            Transfer name on blockchain
        """

        url = self.base_url + "/users/" + username + "/update"

        owner_pubkey = get_pubkey_from_privkey(owner_privkey)

        payload = {
            'transfer_address': transfer_address,
            'owner_pubkey': owner_pubkey
            }

        resp = self._post_request(url, payload)

        try:
            unsigned_tx = resp['unsigned_tx']
        except:
            return resp

        # sign all unsigned inputs
        signed_tx = sign_all_unsigned_inputs(owner_privkey, unsigned_tx_hex)

        return self.broadcast_transaction(signed_tx)
