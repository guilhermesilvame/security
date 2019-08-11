# The purpose of this script is to find database backup files and backups of websites

# Usage
# -----
# download_backup.py [target url] [words]
# 
# download_backup.py
# download_backup.py http://example.com
# download_backup.py http://example.com word1,word2,...

import sys
import requests
from urllib.parse import urlparse
from collections import OrderedDict

from includes.functions import url_exists

# all the urls combined by this script will be added to this list
urls = []

# words are optional, and they should contain all the words related to the target, such as product names, company names, etc.
# don't use spaces in words, if you need to concatenate two or more words, use underscore or hyphen.
targets = [
  {
    'url' : 'http://example.com/',
    'words' : [
    ],
  },
]

if len(sys.argv) > 1:
  target = sys.argv[1]
  if len(sys.argv) == 3:
    words = sys.argv[2].split(',')
  else:
    words = []
  targets = [
    {
      'url' : target,
      'words' : words,
    },
  ]

with open('wordlists/wordlist_backup_folders.txt') as folders_file:
  folders = folders_file.read().splitlines()

with open('wordlists/wordlist_backup_files.txt') as files_file:
  files = files_file.read().splitlines()

with open('wordlists/wordlist_backup_extensions.txt') as extensions_file:
  extensions = extensions_file.read().splitlines()
        
print('\nPlease wait while we build the url list...\n')

for target in targets:
  uri = urlparse(target['url'])
  base_url = uri.scheme + '://' + uri.netloc
  result = url_exists(base_url)
  if result[0] == False:
    print('The target url \'' + base_url + '\' does not exist')
  else:
    words = []
    words.append(uri.netloc)
    words = words + uri.netloc.split('.') + target['words'] + files
    words = list(OrderedDict.fromkeys(words))
    for folder in [ '' ] + folders:
      if (folder == ''):
        folder_url = base_url + '/'
      else:
        folder_url = base_url + '/' + folder + '/'
      result = url_exists(folder_url)
      if result[0] == False:
        continue
      for word in words:
        for extension in extensions:
          url = folder_url + word + extension
          urls.append(url)

    # print all urls
    #for url in urls:
      #print(url)

    # log file to register the http code of each url
    log_file = open('download_backup.log', 'w+')

    for url in urls:
      result = url_exists(url)
      status_code = result[1]
      if result[0] == True:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')
        if (status_code == 200):
          print('**********FOUND**********: ', url)
          print()
      else:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')

    print('\nFinished\n')
