#!/usr/bin/python3
""" fetch data from ressource
"""

from urllib import request

req = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode()}")
