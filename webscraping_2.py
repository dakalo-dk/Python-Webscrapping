from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/detail_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
items = soup.find_all("div", class_="card mt-4 my-4")
for item in items:
    itemName = item.find("h3", class_="card-title").text
    itemPrice = item.find("h4").text
    itemDescription = item.find("p", class_="card-text").text
    print("Name: ",itemName, "\nPrice: ",itemPrice,"\nDescription: ",itemDescription)
