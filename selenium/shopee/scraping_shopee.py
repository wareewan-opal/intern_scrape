from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'\Users\wareewanpongpunchaikul\Desktop\chromedriver_mac_arm64\chromedriver')
driver.get('https://shopee.co.th')

# pop-up shopee
thai_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()

close_button = driver.execute_script(
    'return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()