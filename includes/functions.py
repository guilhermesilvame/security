import requests
from datetime import timedelta

def daterange(start_date, end_date):
  for n in range(((end_date - start_date).days)):
    yield start_date + timedelta(n)

def url_exists(url):
  try:
    r = requests.head(url, allow_redirects=True, timeout=5)
    status_code = r.status_code
    if (status_code == 404):
      return ( False, status_code )
    else:
      return ( True, status_code )
  except requests.exceptions.RequestException:
    return ( False, -1 )
