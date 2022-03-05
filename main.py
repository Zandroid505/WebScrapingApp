#
# Example file for retrieving data from the internet
#

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd

# pd.set_option('display.max_colwidth', 500)
import time
import requests


def main():
    # weburl = urllib.request.urlopen("https://www.instagram.com/kconomon/")
    # print(webUrl.getcode())
    # data = webUrl.read()
    file = open("webScrape.txt", "w")

    weburl = requests.get("https://weather.com/")
    soup = bs(weburl.text, "html.parser")
    links = soup.find_all('span')
    file.write(str(links))
    time.sleep(3)

    # soup = bs(webUrl.content)
    # print(soup)
    # soup.find_all(class='QGPIr')

    # titleString = soup.title.string
    # print(titleString)


if __name__ == "__main__":
    main()
