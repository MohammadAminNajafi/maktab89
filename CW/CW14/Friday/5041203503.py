import requests
from bs4 import BeautifulSoup

URL = "https://s2.filedn.ir/www.skyroom.online/8615/ee98c9d8-6b95-4d89-b2a0-491ca27fac68/2212281422.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())

list1 = soup.find_all("h2")

#print(list1)

for i in list1: 

    print(i.text)
