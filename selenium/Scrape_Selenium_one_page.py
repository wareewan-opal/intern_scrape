#Import modules
from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.common.by import By

#Set directory
path = '/Users/wareewanpongpunchaikul/Desktop/Scraping/selenium' #กำหนด folder ที่จะให้ระบบทำงาน
os.chdir(path) #รัน Code เพื่อสั่งให้ระบบทำงานบน folder ที่ต้องการ

#Open webdriver 
driver = webdriver.Chrome(path+"chromedriver.exe")
# driver.get('https://eshop-prices.com/games/popular?currency=THB')

# for page in range(1,3,1):
#     page_url = 'https://eshop-prices.com/games/popular?currency=THB' +str(page)
#     driver.get(page_url)
# #Get Data games_name , descriptions_game , prices_game 
#     games_name = driver.find_elements(By.CLASS_NAME, 'games-list-item-title')
#     descriptions_game = driver.find_elements(By.CLASS_NAME,'games-list-item-description')
#     prices_game = driver.find_elements(By.CLASS_NAME,'price-tag')
for page in range(1,3,1):
    page_url = 'https://eshop-prices.com/games/popular?currency=THB&page='+str(page)
    driver = webdriver.Chrome(path+"chromedriver.exe")
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    #Get Data games_name , descriptions_game , prices_game 
    games_name = driver.find_elements(By.CLASS_NAME, "games-list-item-title")
    descriptions_game = driver.find_elements(By.CLASS_NAME,"games-list-item-description")
    prices_game = driver.find_elements(By.CLASS_NAME,"price-tag")

    for i in range(len(games_name)):
    #วนลูปเพื่อเอาค่าอื่นๆใน class นี้ออกมาด้วย
        Games_names=[name.text for name in games_name]
        Descriptions_game=[description.text for description in descriptions_game]
        Prices_game=[price.text for price in prices_game]


#Convert to table (DataFrame) ตั้งชื่อ Columns ว่า MovieNames และ Ratings
DF_IMDb=pd.DataFrame({'Games_names':Games_names , 'Descriptions_game':Descriptions_game, 'Prices_game':Prices_game})
#Export to Excel
DF_IMDb.to_excel('test_selenium_list_game.xlsx')