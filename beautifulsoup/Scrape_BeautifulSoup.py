import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://eshop-prices.com/games/popular?currency=THB"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
contents_data = soup.find_all("div",class_ = "games-list well")
class alldata():
    def getnames():
        list_getname = []
        for content_data in contents_data:
            games_name = content_data.find_all("h5")
        for game_name in games_name:
            text = game_name.text
            list_getname.append(text)
        return list_getname
    def getdescription():
        list_getdes = []
        for content_data in contents_data:
            descriptions_game = content_data.find_all("p",class_="games-list-item-description")
        for description_game in descriptions_game:
            text = description_game.text
            list_getdes.append(text)
        return list_getdes
    def getprices():
        list_getprice = []
        for content_data in contents_data:
            prices_game = content_data.find_all("span",class_="price-tag")
        for price_game in prices_game:
            text = price_game.text
            list_getprice.append(text)
        return list_getprice

# print(alldata.getnames())
# print("------------------------")
# print(alldata.getdescription())
# print("------------------------")
# print(alldata.getprices())


df = pd.DataFrame({
    'Game_Name': alldata.getnames(),
    'Descriptions_game': alldata.getdescription(),
    'Price_game': alldata.getprices()
})
print(df)

df.to_csv('test_BeautifulSoup_list_games.csv')