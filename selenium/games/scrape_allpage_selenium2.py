# importing necessary packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import xlsxwriter

# for holding the resultant list
element_list = []
  
for page in range(1, 3, 1):
    page_url = "https://eshop-prices.com/games/popular?currency=THB&page=" + str(page)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME,"games-list-item-title")
    price = driver.find_elements(By.CLASS_NAME,"price-tag")
    description = driver.find_elements(By.CLASS_NAME,"games-list-item-description")
    # rating = driver.find_elements(By.CLASS_NAME,"ratings")
  
    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text])
  
with xlsxwriter.Workbook('result_lol.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)

print(element_list)
print(page_url)
#closing the driver
driver.close()