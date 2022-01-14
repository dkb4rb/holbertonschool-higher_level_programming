#!/usr/bin/python3
"""
Import libraries
"""
from urllib import request

url = 'https://intranet.hbtn.io/status'


def new_request():
    """ Representation request header function"""
    reqt = request.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


""" Declare the flush to program """
if __name__ == "__main__":
    new_request()
