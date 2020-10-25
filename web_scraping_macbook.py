import lxml
from bs4 import BeautifulSoup
import requests
from playsound import playsound
from multiprocessing import Process

url = "https://www.incredible.co.za/13-inch-macbook-air-1-1ghz-quad-core-10th-gen-i5-512gb-gold"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
macbook = soup.find("div", class_="product-info-left-row product-col-block product-info-left-row-meta")

macbook_version = macbook.h1.text #find macbook version from the link provided
macbook_specs = macbook.ul.text #gives the specs of the macbook
macbook_price = soup.find("span", class_="price").text #gives you the price in ZAR

macbook_price = float("".join((macbook_price.strip("R")).split(","))) #convert the price to a float number

#check if the price of the macbook is below your desired price
if macbook_price <= 24000.00:
    
    def game(sound):
        playsound(sound) #plays the sound you provided

    if __name__ == "__main__":
        process = Process(target = game, args = (r'sound.mp3',)) #this mp3 file will play if condition is met
        process.start()

        print(macbook_version)
        print("\nMacBook Specifications:")
        print(macbook_specs)
        print("\nPrice: R{0:.2f}".format(macbook_price))
        print()

        input("press ENTER to stop playback ") #press Enter from the keyboard to stop the mp3 
        process.terminate()
