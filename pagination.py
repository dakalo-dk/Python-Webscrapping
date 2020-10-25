from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

pages = soup.find("ul",class_="pagination")
urls = []
links = pages.find_all("a",class_="page-link")
count = 1
for link in links:
    pageNumber = int(link.text) if link.text.isdigit() else None
    if pageNumber != None:
        x = link.get("href")
        urls.append(x)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    items = soup.find_all("div",class_="col-lg-4 col-md-6 mb-4")
    
    for item in items:
        itemName = item.find("h4",class_="card-title").text.strip("\n")
        itemPrice = item.find("h5").text
        print(count, ") Item Name: ",itemName," and Item Price: ",itemPrice)
        count = count+1

