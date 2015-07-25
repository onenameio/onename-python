#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2015 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

from lib.client import Client

ONENAME_API_ID = ''
ONENAME_API_SECRET = ''

if __name__ == '__main__':

    c = Client(ONENAME_API_ID, ONENAME_API_SECRET)

    print c.get_user('albertwenger')
