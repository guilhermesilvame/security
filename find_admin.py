# The purpose of this script is to find admin modules

# Usage
# -----
# download_admin.py [target]
# 
# download_admin.py
# download_admin.py http://example.com
# 
# Parameters
# ----------
# [target] parameter is a valid url of the target.
# 
# Tips
# ----
# run the script after midnight and come back in one hour.
import sys
import requests
from urllib.parse import urlparse
from collections import OrderedDict

from includes.functions import url_exists

# all the urls combined by this script will be added to this list
urls = []

targets = [
  {
    'url' : 'http://example.com/',
  },
]

if len(sys.argv) == 2:
  target = sys.argv[1]
  targets = [
    {
      'url' : target,
    },
  ]

with open('wordlists/wordlist_admin_folders.txt') as admin_file:
  admin = admin_file.read().splitlines()
          
print('\nPlease wait while we build the url list...\n')
