# The purpose of this script is to find database dated backup files and dated backups of websites

# Usage
# -----
# find_dated_backup.py [target] [words]
# 
# find_dated_backup.py
# find_dated_backup.py http://example.com
# find_dated_backup.py http://example.com word1,word2,...
# 
# Parameters
# ----------
# [target] parameter is a valid url of the target.
# 
# [words] parameter is optional, and it should contain one or more words separated by comma.
# words are common names related to the target, such as product names, service names, company names, etc.
# try not using spaces in words, if you have a composite word, replace the spaces by underscore or hyphen.
# 
# Dependencies
# ------------
# tldextract - https://github.com/john-kurkowski/tldextract
# 
# Tips
# ----
# run the script after midnight, go to sleep and come back in the morning.

import sys
import requests
from urllib.parse import urlparse
from collections import OrderedDict
from datetime import date

from includes.functions import url_exists, daterange, domain_words

# all the urls combined by this script will be added to this list
urls = []

targets = [
  {
    'url' : 'http://example.com/',
    'words' : [
    ],
  },
]

interval = {
  'start_date' : date(date.today().year - 10,1,1),
  'end_date' : date.today()
}

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

with open('wordlists/wordlist_dated_backup_extensions.txt') as extensions_file:
  extensions = extensions_file.read().splitlines()

with open('wordlists/wordlist_backup_dates.txt') as dates_file:
  dates = dates_file.read().splitlines()
          
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
    words = words + domain_words(uri.netloc) + target['words']
    words = list(OrderedDict.fromkeys(words))
    for folder in [ '' ] + folders:
      if folder == '':
        folder_url = base_url + '/'
      else:
        folder_url = base_url + '/' + folder + '/'
      result = url_exists(folder_url)
      if result[0] == False:
        continue
      for dr in daterange(interval['start_date'], interval['end_date']):
        for word in words:
          for extension in extensions:
            for d in dates:
              url = folder_url + word + dr.strftime(d) + extension
              urls.append(url)
              url = folder_url + 'backup_' + word + dr.strftime(d) + extension
              urls.append(url)
              url = folder_url + 'bkp_' + word + dr.strftime(d) + extension
              urls.append(url)
              url = folder_url + 'backup_' + dr.strftime(d) + extension
              urls.append(url)
              url = folder_url + 'bkp_' + dr.strftime(d) + extension
              urls.append(url)

    # print all urls
    #for url in urls:
      #print(url)

    # log file to register the http code of each url
    log_file = open('find_dated_backup.log', 'w+')

    for url in urls:
      result = url_exists(url)
      status_code = result[1]
      content_type = result[2]
      if result[0] == True:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')
      else:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        log_file.write(url + ' (' + str(status_code) + ')\n')
      if status_code != 404 and status_code != -1 and content_type[0:9] != 'text/html':
        # found file
        print('\nFOUND:', url, '\n')
        found_file = open('found.log', 'a+')
        found_file.write(url + ' (' + str(status_code) + ')\n')
        found_file.close()
  
    print('\nFinished\n')
