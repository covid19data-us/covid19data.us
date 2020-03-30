import requests
import sys
import json

# Useage --> CLI: python http://api.covid19data.us "YOUR QUERY"

response = requests.get('{0}/api/v1/query'.format(sys.argv[1]),
    params={'query': sys.argv[2]})
results = response.json()

def jsonprint(obj):
    # format the JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jsonprint(response.json())
