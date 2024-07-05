#!/usr/bin/python3
""" Send data post
"""

import sys
from urllib import request, parse


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    value = {"email": email}
    data = parse.urlencode(value)
    data = data.encode('ascii')

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode())
