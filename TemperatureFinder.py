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


class TemperatureFinder:
    def __init__(self, ):
        self.city = ""

    def plot_graph(self, dictionary, city):
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
        # plt.show()

        return plt

    # User HTML parser to retrieve temperature
    def retrieve_data(self, dates, temperatures):
        forecast = {}
        for i in range(10):
            currdate = dates[i + 1].text
            currtemperature = int(temperatures[i + 1].text[:-1])
            forecast.update({currdate: currtemperature})

        return forecast

    def google_query(self):
        query = self.city + " 10-Day Weather Forecast"

        # search for city on weather.com
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            return requests.get(j)

    def manager(self):
        # city = input from user
        self.city = input("Type in a city to find the 10-day forecast: ")

        url = self.google_query()

        # weburl = url of weather.com for particular city
        soup = bs(url.text, "html.parser")

        # Retrieving the dates
        urldates = soup.find_all('h2', attrs={'class': 'DetailsSummary--daypartName--2FBp2'})
        # Retrieving the temperatures
        urltemperatures = soup.find_all('span', attrs={'class': 'DetailsSummary--highTempValue--3Oteu'})

        forecast = self.retrieve_data(urldates, urltemperatures)

        return self.plot_graph(forecast, self.city)