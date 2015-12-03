from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup

# http://www.uvm.edu/directorylisting/rerickso
browser = webdriver.Firefox()  
html_source = ""
url = "http://www.uvm.edu/directorylisting/"
netID = "rerickso"
for i in range(1):
    url = url + netID
    browser.get(url)
    html_source = browser.page_source  
browser.quit()

soup = BeautifulSoup(html_source)  
print(soup.prettify())
# comments = soup("div", {"class":"postText"})  
# print comments