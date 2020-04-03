import requests
from bs4 import BeautifulSoup

#Change your URL to whatever here
url = "https://covid19data.com"

r=requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser') 
link_list = soup.findAll('a')

for link in link_list:
    if 'href' in link.attrs:
        print (str(link.attrs['href']) + "\n")
