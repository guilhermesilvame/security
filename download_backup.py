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
    
folders = [
  '_archive',
  'archive',
  'archives',
  '_backup',
  'backup',
  'back_up',
  '_bak',
  '_bkp',
  'bkp',
  '_bak',
  'bak',
  '_data',
  'data',
  '_database',
  'database',
  '_db',
  'db',
  '_dump',
  'dump',
  '_files',
  'files',
  'model',
  'models',
  'mongo',
  'mssql',
  'mysql',
  'ora',
  'oracle',
  'postgre',
  'postgresql',
  'postgre_sql',
  'server',
  'sources',
  'sql',
  'tables',
  '_temp',
  'temp',
  '_tmp',
  'tmp',
  '_zip',
  'zip',
  'zips',
  '_rar',
  'rar',
]

files = [
  'archive',
  '_backup',
  'backup',
  'backup_all',
  'backup_cassandra',
  'backup_controller',
  'backup_controllers',
  'backup_config',
  'backup_configs',
  'backup_data',
  'backup_database',
  'backup_db',
  'backup_db2',
  'backup_firebird',
  'backup_full',
  'backup_html',
  'backup_maria',
  'backup_mariadb',
  'backup_maria_db',
  'backup_mdb',
  'backup_model',
  'backup_models',
  'backup_mongo',
  'backup_mongodb',
  'backup_mongo_db',
  'backup_mssql',
  'backup_mysql',
  'backup_my',
  'backup_myadmin',
  'backup_ora',
  'backup_oracle',
  'backup_postgre',
  'backup_postgresql',
  'backup_postgre_sql',
  'backup_root',
  'backup_script',
  'backup_scripts',
  'backup_server',
  'backup_site',
  'backup_source',
  'backup_sourcecode',
  'backup_source_code',
  'backup_sources',
  'backup_sql',
  'backup_sqladmin',
  'backup_sqlserver',
  'backup_sql_server',
  'backup_sqlsrv',
  'backup_src',
  'backup_storage',
  'backup_store',
  'backup_sybase',
  'backup_sys',
  'backup_system',
  'backup_tables',
  'backup_view',
  'backup_views',
  'backup_website',
  'backup_wwwroot',
  'bak',
  'bakup',
  'bd_dump',
  'bkp',
  'bkp_all',
  'bkp_controller',
  'bkp_controllers',
  'bkp_full',
  'bkp_model',
  'bkp_models',
  'bkp_mysql',
  'bkp_my',
  'bkp_myadmin',
  'bkp_ora',
  'bkp_oracle',
  'bkp_root',
  'bkp_schema',
  'bkp_schemas',
  'bkp_script',
  'bkp_scripts',
  'bkp_server',
  'bkp_site',
  'bkp_source',
  'bkp_sourcecode',
  'bkp_source_code',
  'bkp_sources',
  'bkp_sql',
  'bkp_sqladmin',
  'bkp_sqlserver',
  'bkp_src',
  'bkp_store',
  'bkp_storage',
  'bkp_sybase',
  'bkp_sys',
  'bkp_system',
  'bkp_tables',
  'bkp_website',
  'bkp_wwwroot',
  'cassandra',
  'config',
  'configs',
  'configuration',
  'conn',
  'connect',
  'connection',
  'control',
  'controller',
  'controllers',
  'data',
  'database',
  'datfiles',
  'db',
  'db2',
  'default',
  'demo',
  'dev',
  'develop',
  'development',
  'dirs',
  'dump',
  'dumpdb',
  'dump_db',
  'firebird',
  'httpd',
  'httpd.conf',
  'httpd_conf',
  'index',
  'main',
  'maria',
  'mariadb',
  'maria_db',
  'model',
  'models',
  'mongo',
  'mongodb',
  'mongo_db',
  'my',
  'myadmin',
  'mysql',
  'mssql',
  'node',
  'oracle',
  'phpmyadmin',
  'postgre',
  'postgresql',
  'postgre_sql',
  'pub',
  'public',
  'public_html',
  'root',
  'schema',
  'schemas',
  'server',
  'site',
  'source',
  'source_code',
  'src',
  'system',
  'view',
  'views',
  'web',
  'web.config',
  'webconfig',
  'web_config',
  'www',
  'wwwroot',
]

extensions = [
  '.backup',
  '.bak',
  '.bkp',
  '.bz',
  '.bz2',
  '.cfg',
  '.conf',
  '.config',
  '.dat',
  '.data',
  '.db',
  '.db2',
  '.dbs',
  '.dump',
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
  '.pwd',
  '.rar',
  '.sav',
  '.sql',
  '.src',
  '.swf',
  '.sys',
  '.tar',
  '.tar.bz',
  '.tar.bz2',
  '.tar.gz',
  '.temp',
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
