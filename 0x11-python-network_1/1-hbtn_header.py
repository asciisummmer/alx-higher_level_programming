#!/usr/bin/python3
""" Get info from http header
"""
import sys
import urllib.request

request = urllib.request.Request(sys.argv[1])

with urllib.request.urlopen(request) as response:
    for header_info in response.headers.items():
        if header_info[0] == "X-Request-Id":
            print(header_info[1])
