# Chapter 15: Python Programs as Network Servers


- [Notes](#notes)
  - [Create a Web Server in Python](#create-a-web-server-in-python)
    - [A Tiny Socket-based Server](#a-tiny-socket-based-server)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### Create a Web Server in Python

- The web works via socket connections as seen in [Chapter
  14](../14_PythonProgramsAsNetworkClients/Chapter_14.qmd#consume-the-web-from-python)
- Consider a browser
  - The browser sends a request to server
  - The server receives this on a socket connection
  - Send’s back the request response
- We previously saw that web pages are formatted in HTML and the process
  of requesting a webpage is governed by HTTP
- We’ll examine how these communication processes work through creating
  a small web server

#### A Tiny Socket-based Server

- The below program provides a basic socket connection
- You should be able to navigate to, and request the page via a browser
- A tiny webpage should be seen

## Summary

## Questions and Answers
