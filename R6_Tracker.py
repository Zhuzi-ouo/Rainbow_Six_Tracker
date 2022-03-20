import requests
from bs4 import BeautifulSoup
def R6T(User):
    response=requests.get(f"https://r6.tracker.network/profile/pc/{User}")
    soup=BeautifulSoup(response.text,"html.parser")
    Overview=soup.find_all("div",class_="trn-defstat__value")
    r6usericon=soup.find_all("img")
    R6T.Usericon=r6usericon[1].get("src")
    R6T.Wins=Overview[1].string
    R6T.WIN=Overview[2].string
    R6T.KILLS=Overview[3].string
    R6T.KD=Overview[4].string
