from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# import urllib
import time

########## GET THE NAME OF all users ###########
# Read in the clean data (csv file) and make a dataframe
# Use this dataframe and make a list of unique employee names
df = pd.read_csv(filepath_or_buffer="data/uvm_employee_salary_data_1994-2014.csv")
unique_names = set(df.Name)
# convert the set into a list, so its easier to print
unique_names = list(unique_names)

########### SELENIUM ##############
### Use selenium & webdriver to get desired page
browser = webdriver.Firefox()
browser.get('http://www.uvm.edu/directory')
# assert 'UVM' in browser.title
elem = browser.find_element_by_name('directory_name') # Find the search box
elem.send_keys('Robert Erickson' + Keys.ENTER)

# get the page source 
print ("before timmer")
time.sleep(2)   # need these two second to wait for the javascript to load!
source = browser.page_source
# source = str(source)  # can't convert it into a string
source = source.encode('utf8', 'replace')
# print type(source)
print source

# get the Net Id



browser.quit()