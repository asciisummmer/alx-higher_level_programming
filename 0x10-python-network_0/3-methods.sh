#!/bin/bash
# display allow method
curl -s --head 0.0.0.0:5000/route_4 | grep -i "Allow" | cut -d ":" -f 2 | xargs
