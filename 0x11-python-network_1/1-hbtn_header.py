#!/usr/bin/python3
""" Display X-Request-Id
Usage: ./1-hbtn_header.py <URL>
"""
from urllib import request
import sys


def new_request():
    """ Representation request header function"""
    reqt = request.Request(sys.argv[1])
    with request.urlopen(reqt) as response:
        print(dict(response.headers).get("X-Request-Id"))

""" Declare the flush to program """
if __name__ == "__main__":
    new_request()
