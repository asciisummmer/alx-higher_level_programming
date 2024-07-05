#!/bin/bash
# Get content lenght of body response
curl -i -s "$1" | grep -i "Content-Length" | cut -d " " -f 2
