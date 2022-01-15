#!/bin/bash
# Curl display all methods 
curl -sX DELETE "$1" | grep "Allow" | cut -d " " -f 2-
