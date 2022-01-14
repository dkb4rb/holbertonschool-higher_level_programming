#!/usr/bin/python3
"""
Import libraries
"""
import requests

url = 'https://intranet.hbtn.io/status'
r = requests.get(url)
print(r.headers.get("X-Request-Id"))
