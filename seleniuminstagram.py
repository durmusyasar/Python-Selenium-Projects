from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(10) 
login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep(2)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("kullanıcı_adınız")
password.send_keys("şifreniz")

time.sleep(3)

login2 = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/button")
login2.click()
time.sleep(10)
browser.close()
