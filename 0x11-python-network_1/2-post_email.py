#!/usr/bin/python3
""" Send data post
"""

import sys
from urllib import request, parse


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    value = {"email": email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
