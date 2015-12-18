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

try:
    ONENAME_API_ID = os.environ['ONENAME_API_ID']
    ONENAME_API_SECRET = os.environ['ONENAME_API_SECRET']
except:
    print "credentials not found"

from onename.client import OnenameClient

HEX_PRIV_KEY = os.environ['HEX_PRIV_KEY']

privkey = BitcoinPrivateKey(HEX_PRIV_KEY)

if __name__ == '__main__':

    c = OnenameClient(ONENAME_API_ID, ONENAME_API_SECRET, base_url='http://localhost:5000/v1')

    print c.get_user('albertwenger')

    #print c.get_user_stats()
    print c.update_user('muneeb', {'name': 'muneeb'}, owner_privkey=privkey.to_hex())
    #print c.register_user('clone_43453445353', '19bXfGsGEXewR6TyAV3b89cSHBtFFewXt6')
    #print c.get_user('muneeb')
    #print c.get_dkim('onename.com')
    #print c.get_all_users()
    #print c.register_user('clone61', '4543t3fedvd')
    #print c.get_names_owned('NHDEuS8R45Nz763rNmsCXXxgZxa245LZGF
