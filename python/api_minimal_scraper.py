#!/usr/bin/python
import requests

r = requests.get('http://api.covid19data.us/api/v1/query?query=sum(deaths)')

print r.json()