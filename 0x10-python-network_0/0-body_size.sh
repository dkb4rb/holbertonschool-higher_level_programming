#!/bin/bash
# Curl the file and ip the host 

curl -Is $1 | wc -l
