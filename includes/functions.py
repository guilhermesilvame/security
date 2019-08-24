import requests
from datetime import timedelta
import tldextract

def daterange(start_date, end_date):
  for n in range(((end_date - start_date).days)):
    yield start_date + timedelta(n)

def url_exists(url):
  print(url)
  try:
    r = requests.head(url, allow_redirects=True, timeout=20)
    status_code = r.status_code
    if ('Content-Type' in r.headers):
      content_type = r.headers['Content-Type']
    else:
      content_type = ''
    if status_code == 404:
      return ( False, status_code, content_type )
    else:
      return ( True, status_code, content_type )
  except requests.exceptions.RequestException:
    return ( False, -1, '' )

def load_url(url):
  try:
    r = requests.get(url, allow_redirects=True, timeout=20)
    return r.content.decode('utf-8').split('\n')
  except requests.exceptions.RequestException:
    return []

def domain_words(domain):
  domain_parts = tldextract.extract(domain)
  domain_words = domain_parts.subdomain.split('.') + domain_parts.domain.split('.')
  if 'www' in domain_words:
    domain_words.remove('www')
  for i in range(0,10):
    if 'www' + str(i) in domain_words:
      domain_words.remove('www' + str(i))
  return domain_words

def sanitize_list(string_list):
  return list(filter(None, string_list))