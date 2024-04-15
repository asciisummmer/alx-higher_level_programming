#!/usr/bin/python3

def lookup(obj):
    return sorted([key for key in obj.__dict__])
