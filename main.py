#
# Zakaria Antifit & Kobe Conomon
# March 5th, 2022
#

from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import pandas as pd

try:
    from googlesearch import search
except ImportError:
    print("No module name 'google' found")
# pd.set_option('display.max_colwidth', 500)
import time
import requests


def plot_graph(dictionary, city):
    plt.style.use('_mpl-gallery')

    plt.figure(figsize=(10, 6), tight_layout=True)

    # separating dates and temperatures from dictionary
    for i in range(10):
        temperatures = dictionary.values()

    for i in range(10):
        dates = dictionary.keys()

    # plotting values
    plt.plot(dates, temperatures)
    plt.plot(dictionary.values(), 'o-', linewidth=2)
    plt.title('10-day Forecast for ' + city)
    plt.xlabel('Date')
    plt.ylabel('Temperature (in °F)')
    plt.show()


# User HTML parser to retrieve temperature
def retrieve_data(dates, temperatures):
    forecast = {}
    for i in range(10):
        currdate = dates[i + 1].text
        currtemperature = int(temperatures[i + 1].text[:-1])
        forecast.update({currdate: currtemperature})

    return forecast


def google_query(city):
    query = city + " 10-Day Weather Forecast"

    # search for city on weather.com
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        return requests.get(j)


def main():
    file = open("webScrape.txt", "w")

    # city = input from user
    city = input("Type in a city to find the 10-day forecast: ")

    url = google_query(city)

    # weburl = url of weather.com for particular city
    soup = bs(url.text, "html.parser")

    # Retrieving the dates
    urldates = soup.find_all('h2', attrs={'class': 'DetailsSummary--daypartName--2FBp2'})
    # Retrieving the temperatures
    urltemperatures = soup.find_all('span', attrs={'class': 'DetailsSummary--highTempValue--3Oteu'})

    forecast = retrieve_data(urldates, urltemperatures)

    plot_graph(forecast, city)

    file.write(str(forecast))

    # Use dictionary with date as key and temperature as value

    # Write temperature to file


if __name__ == "__main__":
    main()
