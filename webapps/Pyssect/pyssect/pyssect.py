#!/usr/bin/python

# Parses URLS for parameters and values
# Can brute force directories and files
    
from urllib.parse import urlparse
from urllib.parse import parse_qs
from bs4 import BeautifulSoup
import requests, sys, re
from mimetypes import args
import urllib

url = 'https://notices.rei.com/pub/cc?_ri_=X0Gzc2X%3DYQpglLjHJlYQGlzgrUuDoFwYhOXw7IOJtMkXzet485LP184ezfyh2hio6awBjyN1wWVXtpKX%3DSRSURUSS&_ei_=EuFBWJqUWaLLkAGD46ZqJrUbr5-YyY_DjIDdYqp_nNjkND0ck3O66ynK-LSVPorUrAeMFI2rGCZttWMaKBZQSvV558sdFVYMDViP9dcPMmib5YufWANGVXqcCxEPeLQj4SNfONGEo9LhP7OffEAyVbpvBdVv2Ydrnq-rmSTelxDncLSWBPa-bFxNaDTvBwMg72-TOfEQmwc1M3R0ZInXkZ4VEdDYGpVSeoJWyjEhV4waNiF1EnSMILRw5gu8B4mjP2zF82HTQgzHHsGEVjE6kxgrdvruhsyur-ZFAazYeE9E-advv0MnFZKkxboyAbtWliG91T7j.&_di_=ipunve4fji97i05k16klrmh5pbi629smgv8nbh403qj39ijif7kg'

if len(*args) != 2:
    sys.exit('Define a target url')

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', sys.arg[1])

try:
    urls
except:
    sys.exit('Not a Valid URL format')

class Target:
    'Base class for Target to enumerate'
    #Get Target as input

    target_address = sys.argv[1]

    def __init__(self, targetAddress=target_address, parameters=None, cookies=None,):
        self.targetAddress = targetAddress
        self.parameteters = parameters
        self.cookies = cookies
    #protocol=urlsplit(url[0]), domain=urlsplit(url[1]), path=urlsplit(url[2]), query=urlsplit(url[3]), cookies=None):

    def display(self):
        pass

    def getParams(self,target):
        parsed = urlparse.urlparse(target)
        params = urlparse.parse_qsl(parsed.query)
        


if __name__ == '__main__':
    print("Running...")
    targetURL = Target(sys.argv[1])    
    
'''
# Look for a directory function
# urllib.parse.urljoin(base, url)
# url = fileinput

# Look for a file function
# # Brute Force
# # Exists?
'''