#!/bin/bash
#  Python script that fetches https://alx-intranet.hbtn.io/status
curl -s "$1" | wc -c
