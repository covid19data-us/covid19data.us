import urllib
import requests

#URL for IMHE /latest CSV File -- Cases, ICU capacity, Hospitals, ++
#Base URL: https://covid19.healthdata.org/projections
url = "https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip"

r = requests.get(url)

with open("ihme-covid19.zip", "wb") as f:
    f.write(r.content)

print(r.status_code)

