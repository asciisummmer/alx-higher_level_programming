#!/usr/bin/python3
""" Get info from http header
"""

import sys
from urllib import request


req = request.Request(sys.argv[1])
with request.urlopen(req) as response:
    for header_info in response.headers.items():
        if header_info[0] == "X-Request-Id":
            print(header_info[1])
