import requests
import urllib.parse
from bs4 import BeautifulSoup
import urllib3
from html import unescape
import tomd
import os
import re
import argparse

# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Blinkist username")
parser.add_argument("password", help="Blinkist password")
parser.add_argument("book", help="Book url")
#parser.add_argument("urls", help="Comma delimited list of Blinkist book URLs", type=lambda s: [str(item) for item in s.split(',')])

# extract args
args = parser.parse_args()

# Read username & password
username = args.username
password = args.password
book_url = args.book

print("{0} : {1} : {2}".format(username, password, book_url))

# Session and headers
session = requests.session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3021.0 Safari/537.36'
session.headers['origin'] = 'https://www.blinkist.com'
session.headers['upgrade-insecure-requests'] = "1"
session.headers['content-type'] = "application/x-www-form-urlencoded"
session.headers['accept-encoding'] = "gzip, deflate, br"
session.headers['authority'] = "www.blinkist.com"

# Get CSRF token
login_url="https://www.blinkist.com/en/nc/login"
response = session.get(url=login_url)
soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
csrf_token = soup.find("meta", {"name": "csrf-token"}).attrs["content"]
print("csrf_token: " + csrf_token)

resp = session.post(url=login_url, data={
    "login[email]": username,
    "login[password]": password,
    "login[facebook_access_token]": None,
    "utf8": unescape("%E2%9C%93"),
    "authenticity_token": csrf_token
}, allow_redirects=True)

read_url="https://www.blinkist.com/books/"+book_url
print("read_url: "+read_url)
book = session.get(url=read_url)
book = BeautifulSoup(book.content.decode('utf-8'), "html5lib")
book = book.find("div", {"class": "book__header-container"})
title = book.find("h1", {"class": "book__header__title"}).string.strip()
author = book.find("div", {"class": "book__header__author"}).string.strip()
img = book.find("img")["src"]

print("title: "+title)
print("author: "+author)
print("img: "+img)

read_url="https://www.blinkist.com/en/nc/reader/"+book_url
book = session.get(url=read_url)
book = BeautifulSoup(book.content.decode('utf-8'), "html5lib")
content = str(book.find("article", {
              "class": "shared__reader__blink reader__container__content"}).contents).strip()
content = tomd.convert(content)
content = re.sub('#', '##', content)

output = "# " + title + "\n\n" + author + "\n\n![" + title + "](" + img + ")\n\n" + content
fileName = re.sub(" ", "-", title.lower())
fileName = fileName + ".md"
fileName = os.path.join("blinks", fileName)

with open(fileName, "w", encoding="utf8") as text_file:
    text_file.write(output)

# print(book)
