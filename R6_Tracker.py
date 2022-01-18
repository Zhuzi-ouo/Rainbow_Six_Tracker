User=input ("Enter Your Rainbow Six Username:")
import requests
from bs4 import BeautifulSoup

response=requests.get(f"https://r6.tracker.network/profile/pc/{User}")
soup=BeautifulSoup(response.text,"html.parser")
Overview=soup.find_all("div",class_="trn-defstat__value")
r6usericon=soup.find_all("img")
Usericon=r6usericon[1].get("src")
print ("Wins",Overview[1].string)
print ("WIN %",Overview[2].string)
print ("KILLS",Overview[3].string)
print ("KD",Overview[4].string)
print (Usericon)
