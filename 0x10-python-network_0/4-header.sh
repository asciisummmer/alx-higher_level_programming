#!/bin/bash
# Add request header
curl -s -X GET -H "X-School-User-Id: 98" "$1"
