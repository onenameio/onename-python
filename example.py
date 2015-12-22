#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2015 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

import os
import requests
import json
from pybitcoin import BitcoinPrivateKey

from registrar.wallet import HDWallet

try:
    ONENAME_API_ID = os.environ['ONENAME_API_ID']
    ONENAME_API_SECRET = os.environ['ONENAME_API_SECRET']
except:
    print "credentials not found"

from onename.client import OnenameClient

try:
    HEX_PRIV_KEY = os.environ['HEX_PRIV_KEY']
    wallet = HDWallet(HEX_PRIV_KEY)
except:
    wallet = HDWallet()

if __name__ == '__main__':

    username = "clone_4345"
    profile = {"name": {"formatted": "Clone 4345"},
               "v": "2"}
    owner_address, owner_privkey = wallet.get_keypairs(1, include_privkey=True)[0]


    c = OnenameClient(ONENAME_API_ID, ONENAME_API_SECRET, base_url='http://localhost:5000/v1')
    #c = OnenameClient(ONENAME_API_ID, ONENAME_API_SECRET)

    #print c.get_user_stats()
    #print c.register_user(username, owner_address)
    print c.update_user(username, profile, owner_privkey=owner_privkey)

    #print c.get_user('muneeb')
    #print c.get_dkim('onename.com')
    #print c.get_all_users()
    #print c.register_user('clone61', '4543t3fedvd')
    #print c.get_names_owned('NHDEuS8R45Nz763rNmsCXXxgZxa245LZGF