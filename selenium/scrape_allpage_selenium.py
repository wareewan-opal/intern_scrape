from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import xlsxwriter
import pandas as pd

#Set directory
# path = '/Users/wareewanpongpunchaikul/Desktop/Scraping/selenium' 
#กำหนด folder ที่จะให้ระบบทำงาน
# os.chdir(path) #รัน Code เพื่อสั่งให้ระบบทำงานบน folder ที่ต้องการ

all_datas = []
# range(start, stop, step)
for page in range(1, 3, 1):
        page_url = "https://eshop-prices.com/games/popular?currency=THB&page=" +str(page)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(page_url)
        #Get Data games_name , descriptions_game , prices_game 
        games_name = driver.find_elements(By.CLASS_NAME, "games-list-item-title")
        descriptions = driver.find_elements(By.CLASS_NAME,"games-list-item-description")
        prices = driver.find_elements(By.CLASS_NAME,"price-tag")
    
        for i in range(len(games_name)):
            all_datas.append([games_name[i].text, 
                      descriptions[i].text,
                      prices[i].text
                      ])
    
with xlsxwriter.Workbook('selenium_list_game.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(all_datas):
        worksheet.write_row(row_num, 0, data)

print(page_url)
print(all_datas)
driver.close()                          