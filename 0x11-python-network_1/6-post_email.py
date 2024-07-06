#!/usr/bin/python3
""" Send post data
"""

import sys
import requests

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    res = requests.post(url, data={'email': email})
    print(res.text)
