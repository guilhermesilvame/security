# The purpose of this script is to find database backup files and backups of websites

import requests
from urllib.parse import urlparse
from collections import OrderedDict

def url_exists(url):
  try:
    r = requests.head(url, allow_redirects=True, timeout=5)
    status_code = r.status_code
    if (status_code == 404):
      return ( False, status_code )
    else:
      return ( True, status_code )
  except requests.exceptions.RequestException as e:
    return ( False, -1 )

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
      for file in words:
        for extension in extensions:
          url = folder_url + file + extension
          urls.append(url)

    # print all urls
    #for url in urls:
    #  print(url)

    # log file to register the http code of each url
    file = open('download_backup.log', 'w+')

    for url in urls:
      result = url_exists(url)
      status_code = result[1]
      if result[0] == True:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        file.write(url + ' (' + str(status_code) + ')\n')
        if (status_code == 200):
          print('**********FOUND**********: ', url)
          print()
      else:
        print('Retrieving url:', url, '(' + str(status_code) + ')')
        file.write(url + ' (' + str(status_code) + ')\n')

    print('\nFinished\n')
