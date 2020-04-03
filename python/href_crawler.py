from bs4 import BeautifulSoup
import urllib
import re
import requests

#//Open a file called crawl.txt, it will create one if non exists.
#//Results will print to console as well and be saved to that file.
#//The file will be overwitten everytime the script is ran.
with open ('crawl.txt', 'w+') as file:
    pass #Pass through

#// Act as a user (browser), making request appear as legitimate as possible
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

#// Putting the sites here that you want to crawl
sites = [
    'http://www.cbsnews.com',
    'http://news.abs-cbn.com',
    'https://www.bbc.com/news/coronavirus',
]

#// standard error handling if .get url hits a snag
for url in sites:
    try: 
        response = requests.get(url)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)


#//A for Loop, against "sites" list above, then print a console message for visually pleasing reasons.
#//print statements can be removed if needed.
#//In source = important to add the '.text' 
#//Using a regular expression to look at the href and perform some match
#//change the re.compile [regular expression to ".*whatever you want.*"]
for url in sites:
    print ("--------------------------------------")
    print ("Reading Site:", url)
    print ("--------------------------------------")    
    source = requests.get(url, headers=headers, timeout=5).text #//Beautiful Soup 
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.findAll('a', href=re.compile(".*covid.*")) [0:10] #//[10] number of results, change as needed

    with open ('crawl.txt', 'a') as file: #//open file
        for link in links:
            print (str(link.get('href') + '\n'))
            file.write(str(link.get('href') +'\n'))#//Write to the file
