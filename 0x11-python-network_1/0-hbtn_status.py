#!/usr/bin/python3
"""
Import libraries
"""
from urllib import request

url = 'https://intranet.hbtn.io/status'


def new_request():
    """ Representation request header function"""
    reqt = request.Request(url)
    response = request.urlopen(reqt)
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))


""" Declare the flush to program """
if __name__ == "__main__":
    new_request()
