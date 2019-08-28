from selenium import webdriver
import loginInfo
import time


browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/form/div[3]/div/p/a")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)


login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")

login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='search-query']")
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")



searchArea.send_keys("#yazilimayolver")

searchButton.click()

time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
tweets = []

elements = browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1

browser.close()