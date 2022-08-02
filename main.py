from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)

url = "http://eaapp.somee.com"
driver.get(url)
input_search=driver.find_element(By.NAME,"q")
input_search.send_keys("котики")
input_search.send_keys(Keys.ENTER)