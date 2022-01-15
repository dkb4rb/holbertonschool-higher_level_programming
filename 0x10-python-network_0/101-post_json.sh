#!/bin/bash
# send  all reques to given URL 
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
