import requests
from bs4 import BeautifulSoup

url = "https://spidyquotes.herokuapp.com/page/2/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
quotes = soup.find_all("span",class_="text")
authors = soup.find_all("small",class_="author")
tags = soup.find_all("div",class_="tags")
count=1
for i in range(len(quotes)):
    print(count,") ",quotes[i].text,"\n",authors[i].text)
    count= count + i
    quoteTags = tags[i].find_all("a",class_="tag")
    for quoteTag in quoteTags:
        print(quoteTag.text)
