# stolen from https://github.com/theghostofc/Blinkist-Daily-Scraper
# to run, $ python3 blinkist_daily_scraper.py

# coding: utf-8
from bs4 import BeautifulSoup
from datetime import datetime
import os
import tomd
import urllib3
import re
import pathlib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'}
http = urllib3.PoolManager(10, headers = headers)
urllib3.disable_warnings()

def get_element_from_request(url, element, class_):
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data.decode('utf-8'), "html5lib")
    return soup.find(element, class_ = class_)

# Get meta data
print("getting daily page")
container = get_element_from_request('https://www.blinkist.com/nc/daily', 'div', "daily-book__grid")

title = container.find('h3', 'daily-book__headline').string.strip()
author = container.find('div', 'daily-book__author').string.strip()[3:]
description = container.find('div', 'book-tabs__content-inner').p.contents[1]
cta = container.find('a', 'cta')['href']
img_url = container.find('img')['src']

date = datetime.now().strftime('%Y%m%d')

bookfile = "blinkist-daily/" + date + "-" + re.sub(" ", "-", title.lower()) + "-by-" + re.sub(" ", "-", author.lower()) + ".md"

if pathlib.Path(bookfile).exists():
    print(bookfile + " exists")
    exit()

# Get actual content
print("get content")
article = get_element_from_request(f'https://www.blinkist.com{cta}', 'article', 'shared__reader__blink reader__container__content')

# Convert to markdown, add source and dump to a file
print("convert markdown")
output = f'![{title}]({img_url})\n# {title}\n*{author}*\n\n>{description}\n\n{tomd.convert(str(article).strip())}\n\nSource: [{title} by {author}](https://www.blinkist.com{cta})'

commitMessage = f'b: {title}'

print("writing " + bookfile)
with open(bookfile, "w", encoding="utf8") as text_file:
    text_file.write(output)

os.system(f'git add "{bookfile}"')
os.system(f'git commit -m "{commitMessage}"')
os.system(f'git push')
