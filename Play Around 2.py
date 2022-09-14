from selenium import webdriver
import time
import re
web = 'https://sports.everygame.eu/en/Bets/Baseball/4' #you can choose any other league
path = r"C:\Users\alexg\Downloads\chromedriver.exe" #introduce your file's path inside '...'


driver = webdriver.Chrome(path)
driver.get(web)
#location pop up
'''time.sleep(10)
deny = driver.find_element_by_xpath('//*[@id="pa-deny-btn"]')
deny.click()'''
#sign up bonus pop up
'''time.sleep(25)
accept = driver.find_element_by_xpath('//*[@id="ConversionMessage"]/div/div/div/div[1]/a')
accept.click()'''

#useful regex
#-[0-9]{3}

centercol = driver.find_element_by_xpath('//*[@id="center-col"]')
print(centercol.text)

exp = 'OUTRIGHT\n*'
p = re.compile(exp)
line = centercol.text
m = p.search(line)
print(m)
print("hello")
