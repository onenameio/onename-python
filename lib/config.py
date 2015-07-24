# -*- coding: utf-8 -*-
"""
    API Client
    ~~~~~
    :copyright: (c) 2015 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

import os

try:
    ONENAME_API_ID = os.environ['ONENAME_API_ID']
    ONENAME_API_SECRET = os.environ['ONENAME_API_SECRET']
except:
    ONENAME_API_ID = ONENAME_API_SECRET = None


try:
    from config_local import ONENAME_BASE_URL
except:
    ONENAME_BASE_URL = "https://api.onename.com/v1"
