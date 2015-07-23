#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2015 by Halfmoon Labs, Inc.
    :license: MIT, see LICENSE for more details.
"""

from lib.client import Client

if __name__ == '__main__':

    c = Client()

    print c.get_stats()
    #print c.get_all_users()
