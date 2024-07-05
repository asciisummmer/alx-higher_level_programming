#!/usr/bin/python3
""" Get info from http header
"""

import sys
from urllib import request


req = request.Request(sys.argv[1])
with request.urlopen(req) as response:
    print(response.headers.get("X-Request-Id"))
