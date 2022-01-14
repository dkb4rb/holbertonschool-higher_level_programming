#!/usr/bin/python3
"""
Import libraries
"""
from urllib import request

url = 'https://intranet.hbtn.io/status'
reqt = request.get(url)
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
