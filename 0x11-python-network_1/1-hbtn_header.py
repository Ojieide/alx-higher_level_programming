#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""

from urllib import request
from sys import argv
if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
