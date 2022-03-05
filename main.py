#
# Zakaria Antifit & Kobe Conomon
# March 5th, 2022
#

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd

# pd.set_option('display.max_colwidth', 500)
import time
import requests


def main():
    file = open("webScrape.txt", "w")
    weathersite = requests.get("https://weather.com/")
    # city = input from user
    # search for city on weather.com
    # weburl = url of weather.com for particular city
    soup = bs(weathersite.text, "html.parser")
    links = soup.find_all('span', "CurrentConditions--tempValue--3a50n")
    retrieveddata = str(links)
    # for(iterarte from end of string to temperature [ex:83°]
        # temperature = read temperature from string

    # Write temperature to file

    print(retrieveddata)
    time.sleep(3)


if __name__ == "__main__":
    main()
