import webbrowser

def main():
 # Change browser here 'chrome', 'firefox', etc.
    browser = webbrowser.get(using=None)

    urls = [
        "https://www.google.com/search?q=covid+19",
        "https://search.yahoo.com/search?p=covid+19",
        "http://graphs.covid19data.us",
        "https://www.covid19data.com",
        "https://www.ninjavirus.com",
        "https://covid19.healthdata.org/projections",
        "https://www.linkedin.com"
        ]

    first = True
    for url in urls:
       # if first:
        browser.open(url, new=1)
          #  first = False
        #else:
          #  browser.open_new_tab(url)

if __name__ == '__main__':
    main()

