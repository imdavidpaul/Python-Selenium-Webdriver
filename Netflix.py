from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.netflix.com/in/title/80057918")
time.sleep(2)

desc = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]").text
cast = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/section[4]/div[3]/div").text
time.sleep(3)

print("Description: ", desc)
print("Cast: ", cast)

driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/section[2]/div[2]/ul/li[1]").click()




