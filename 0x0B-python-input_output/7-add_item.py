#!/usr/bin/python3

"""Module to load json"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    import sys
    import json

    args = sys.argv[1:]
    filename = "add_item.json"
    if len(args) == 0:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([], f)
    value = load_from_json_file(filename)
    value += args
    save_to_json_file(value, filename)
