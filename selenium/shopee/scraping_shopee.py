from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=r'\Users\wareewanpongpunchaikul\Desktop\chromedriver_mac_arm64\chromedriver')
driver.get('https://shopee.co.th')

# pop-up shopee
thai_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()

close_button = driver.execute_script(
    'return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()
time.sleep(5)

firstpage = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[3]/div[3]')
firstpage = driver.page_source

soup = BeautifulSoup(firstpage,features="html.parser")
product_names = soup.find_all("div",class_="WSS36c V2HAG1")
price_products = soup.find_all("div",class_="rFVivR i2AHh8")
sale_products = soup.find_all("div",class_="YqXPle fVGgj5")

print(product_names)
class alldata():
    def getnames():
        list_getname = []
        for product_name in product_names:
            text = product_name.text
            list_getname.append(text)
        return list_getname
    def getprices():
        list_getprice = []
        for price_product in price_products:
            text = price_product.text
            list_getprice.append(text)
        return list_getprice
    def getsales():
        list_getsale = []
        for sale_product in sale_products:
            text = sale_product.text
            list_getsale.append(text)
        return list_getsale
print(alldata.getnames())
print(alldata.getprices())
print(alldata.getsales())

# shopee_data = pd.DataFrame({'Product_Names': alldata.getnames(),
#                             'Product_Prices': alldata.getprices(),
#                             'Sale_Products':alldata.getsales()}
#                           )
# shopee_data.transpose()
# shopee_data
# shopee_data.to_csv('shopee_data.csv')