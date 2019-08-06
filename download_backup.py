# The purpose of this script is to find database backup files and backups of websites

import requests
from urllib.parse import urlparse
from collections import OrderedDict

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

folders = [
  '', # <ROOT>
  '_backup',
  'backup',
  'back_up',
  '_bkp',
  'bkp',
  '_bak',
  'bak',
  'data',
  'database',
  '_db',
  'db',
  '_files',
  'files',
  'zip',
  'rar',
]

files = [
  '_backup',
  'backup',
  'backup_cassandra',
  'backup_data',
  'backup_db',
  'backup_db2',
  'backup_firebird',
  'backup_maria',
  'backup_mariadb',
  'backup_maria_db',
  'backup_mongo',
  'backup_mongodb',
  'backup_mongo_db',
  'backup_mysql',
  'backup_mssql',
  'backup_oracle',
  'backup_postgre',
  'backup_postgresql',
  'backup_postgre_sql',
  'backup_server',
  'backup_site',
  'backup_sql',
  'backup_sqlserver',
  'backup_sql_server',
  'bak',
  'bkp',
  'cassandra',
  'data',
  'database',
  'db',
  'db2',
  'demo',
  'dev',
  'develop',
  'development',
  'firebird',
  'httpd',
  'httpd.conf',
  'httpd_conf',
  'index',
  'main',
  'maria',
  'mariadb',
  'maria_db',
  'mongo',
  'mongodb',
  'mongo_db',
  'mysql',
  'mssql',
  'node',
  'postgre',
  'postgresql',
  'postgre_sql',
  'public',
  'public_html',
  'root',
  'site',
  'source',
  'source_code',
  'oracle',
  'web',
  'web.config',
  'webconfig',
  'web_config',
  'www',
  'wwwroot',
]

extensions = [
  '.bak',
  '.bkp',
  '.bz',
  '.bz2',
  '.conf',
  '.config',
  '.db',
  '.db2',
  '.dat',
  '.inc',
  '.inf',
  '.ini',
  '.json',
  '.ldf',
  '.mdb',
  '.mdf',
  '.new',
  '.old',
  '.ora',
  '.rar',
  '.sav',
  '.sql',
  '.src',
  '.sys',
  '.tar',
  '.tar.bz',
  '.tar.bz2',
  '.tar.gz',
  '.tgz',
  '.tmp',
  '.xml',
  '.zip',
]

for target in targets:
  uri = urlparse(target['url'])
  base_url = uri.scheme + '://' + uri.netloc
  words = []
  words.append(uri.netloc)
  words = words + uri.netloc.split('.')
  words = words + target['words']
  words = words + files
  words = list(OrderedDict.fromkeys(words))
  for folder in folders:
    if (folder == ''):
      folder_exists = True
    else:
      try:
        r = requests.head(base_url + '/' + folder + '/', allow_redirects=True, timeout=5)
        if (r.status_code == 404):
          folder_exists = False
        else:
          folder_exists = True
      except requests.exceptions.RequestException as e:
        folder_exists = False
    if folder_exists == False:
      continue
    for file in words:
      for extension in extensions:
        if folder == '':
          url = base_url + '/' + file + extension
        else:
          url = base_url + '/' + folder + '/' + file + extension
        urls.append(url)

for url in urls:
  print(url)

file = open('download_backup.log', 'w+')
for url in urls:
  try:
    r = requests.head(url, allow_redirects=True, timeout=5)
    print('Retrieving url:', url, '(' + str(r.status_code) + ')')
    file.write(url + ' (' + str(r.status_code) + ')\n')
    if (r.status_code == 200):
      print('**********FOUND**********: ', url)
      print()
  except requests.exceptions.RequestException as e:
    print('Retrieving url:', url, '(ERROR)')
    file.write(url + ' (ERROR)\n')

print()
print('Finished')
