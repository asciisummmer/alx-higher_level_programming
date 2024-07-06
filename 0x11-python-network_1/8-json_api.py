#!/usr/bin/python3
""" check status code
"""

import sys
import requests


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    payload = {'q': q}
    try:
        res = requests.post(url, params=payload)
        json_result = res.json()
        if len(json_result) == 0:
            print("No result")
        else:
            print(f"[{json_result.get('id')}] {json_result.get('name')}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
