#!/bin/bash

#Python RSS Feed Reader with BS4 -just for- Real Python Website RSS Feeds


from bs4 import BeautifulSoup #if you don't have it: pip install beautifulsoup4
import requests
import lxml
import cowsay #pip3 install cowsay


cowsay.cow('Welcome to RealPython RSS Feed Reader')

print("\n\t\t\tWelcome to Real Python Rss Feeds Scraper\n\n")
print("\n\tReal Python is a great blog/website for learning Python. This Python script will scrape the RSS Feeds for you...\n\n\n")


url = requests.get('https://realpython.com/atom.xml')

soup = BeautifulSoup(url.content, 'xml')
entries = soup.find_all('entry')

for entry in entries:
	title = entry.title.text
	summary = entry.summary.text
	link = entry.link['href']
	print(f"\tTitle: {title}\n\nSUMMARY: {summary}\n\n\tLink: {link}\n\n\n\t\t\t\t\t\t\t..................................................\n\n")

print("\tI'll work on a better and more functional version of this project in which you can save the links, titles, summaries in an organized and colorful cli version soon.")


print(cowsay.get_output_string('trex', 'EmreYbs wishes you a lovely day... Bye for now'))
