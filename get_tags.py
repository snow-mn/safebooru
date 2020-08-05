import requests
from bs4 import BeautifulSoup
import re

urlName = "https://safebooru.org/index.php?page=tags&s=list"
# urlName = "https://business.nikkei.com"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")

# elems = soup.find_all("span")

# for elem in elems:
#   try:
#     string = elem.get("class").pop(0)
#     print(string)
#     print(elem.string)
#   except:
#     pass

elems = soup.find_all("table")

for elem in elems:
  try:
    string = elem.get("class").pop(0)
    if string in "highlightable":
      #print(elem)
      print("a")
  except:
    pass

soup = elem
elems = soup.find_all("td")
print(elems)


