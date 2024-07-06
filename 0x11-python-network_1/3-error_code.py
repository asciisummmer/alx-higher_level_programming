#!/usr/bin/python3
""" Manage Http error
"""

import sys
from urllib import request, error


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('UTF-8'))
    except error.HTTPError as e:
        print("Error code:", e.code)
