import pathlib
import requests
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize


def scrape_link(url, file_name):
    current_page = requests.get(url)
    current_file = open(file_name, 'w')
    current_soup = BeautifulSoup(current_page.content, 'html.parser')
    for p in current_soup.select('p'):
        current_file.write(p.get_text() + '\n')


def tokenize_file(file):
    with open(pathlib.Path.cwd().joinpath(file), 'r') as f:
        raw_text = f.read()
    tokens = word_tokenize(raw_text)
    tokens = tokens[25:]
    print(tokens)


URL = 'https://www.pcgamer.com/elden-ring-guide/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
pageText = open('text.txt', 'w')

for p in soup.select('p'):
    pageText.write(p.get_text() + '\n')

link_counter = 0
for link in soup.find_all('a', attrs={'href': re.compile('^https://www.pcgamer.com')}):
    current_link = link.get('href')
    if link_counter < 20 and 'elden' in current_link:
        print(current_link)
        filename = 'file' + str(link_counter + 1) + '.txt'
        scrape_link(current_link, filename)
        link_counter = link_counter + 1
        tokenize_file(filename)
