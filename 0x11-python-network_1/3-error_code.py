#!/usr/bin/python3
""" Manage Http error
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode())
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
