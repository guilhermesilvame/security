# The purpose of this script is to find admin modules

# Usage
# -----
# find_admin.py [target]
# 
# find_admin.py
# find_admin.py http://example.com
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

from includes.functions import url_exists, sanitize_list

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

with open('wordlists/wordlist_admin.txt') as admin_file:
  admin = admin_file.read().splitlines()
          
print('\nPlease wait while we build the url list...\n')

for target in targets:
  uri = urlparse(target['url'])
  base_url = uri.scheme + '://' + uri.netloc
  result = url_exists(base_url)
  if result[0] == False:
    print('The target url \'' + base_url + '\' does not exist')
  else:
    for folder in admin:
      folder_url = base_url + '/' + folder + '/'
      url = folder_url
      urls.append(url)

    # print all urls
    #for url in urls:
      #print(url)

    # log file to register the http code of each url
    log_file = open('find_admin.log', 'w+')

    for url in urls:
      result = url_exists(url)
      status_code = result[1]
      if result[0] == True:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')
      else:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')
      if status_code != 404 and status_code != -1:
        # found file
        print('\nFOUND:', url, '\n')
        found_file = open('found.log', 'a+')
        found_file.write(url + ' (' + str(status_code) + ')\n')
        found_file.close()
  
    print('\nFinished\n')
