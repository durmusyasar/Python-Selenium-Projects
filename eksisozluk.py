from selenium import webdriver
import time, random

browser = webdriver.Firefox()

url = "https://eksisozluk.com/trabzon--48560"

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,1290)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("***********************************\n")
        entryCount += 1



browser.close()
