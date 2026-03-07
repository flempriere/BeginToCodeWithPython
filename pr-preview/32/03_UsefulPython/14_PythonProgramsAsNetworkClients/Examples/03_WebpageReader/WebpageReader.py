"""
Example 14.3 Webpage Reader

A simple program to demonstrate fetching content from a URL
"""

import urllib.request

url = "https://www.robmiles.com"

req = urllib.request.urlopen(url)
for line in req:
    print(line)
