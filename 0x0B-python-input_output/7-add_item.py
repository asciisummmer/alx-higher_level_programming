#!/usr/bin/python3

"""Module to load json"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    save_to_json_file(args, filename)
