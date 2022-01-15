#!/bin/bash
# Curl display all methods 
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
