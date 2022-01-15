#!/bin/bash
# send  all reques to given URL 
curl -s -o /dev/null -w "%{http_code}" "$1"
