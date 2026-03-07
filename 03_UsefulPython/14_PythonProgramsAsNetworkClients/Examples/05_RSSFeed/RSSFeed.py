"""
Example 14.5 RSS Feed

Combines fetching a URL with urllib and passing the XML document with
the XML ElementTree
"""

import urllib.request
import xml.etree.ElementTree as ElementTree

url = "https://www.robmiles.com/journal/rss.xml"

req = urllib.request.urlopen(url)
page = req.read()

doc = ElementTree.fromstring(page)
for item in doc.iter("item"):
    title: str = item.find("title").text  # type: ignore
    print(title.strip())
    description: str = item.find("description").text  # type: ignore
    print("    ", description.strip())
