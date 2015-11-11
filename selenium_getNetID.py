from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import pprint


######### little function to help with searching names
# given a name in this format: Last,First Middle
def getLastFirstNames(str_name):
    last_name = str_name.split(",",2)
    first_name = last_name[1].split(" ", 2)
    first_name = first_name[0]
    last_name = last_name[0]
    name_search = first_name + " " + last_name
    return name_search

########## GET THE NAME OF all users ###########
# Read in the clean data (csv file) and make a dataframe
# Use this dataframe and make a list of unique employee names
df = pd.read_csv(filepath_or_buffer="data/uvm_employee_salary_data_1994-2014.csv")
unique_names = set(df.Name)
# convert the set into a list, so its easier to print
unique_names = list(unique_names)
unique_netID = [] # list that stores all the unique netID

########### SELENIUM ##############
### Use selenium & webdriver to get desired page
browser = webdriver.Firefox()
browser.get('http://www.uvm.edu/directory')
# assert 'UVM' in browser.title
# need to do this for each person!
for i in range(10):
	#get the employee name --> ex. Allen,Linda L.
	# print unique_names[i]
	employee_name = getLastFirstNames(unique_names[i])
	print employee_name
	try:
		browser.get('http://www.uvm.edu/directory')
		elem = browser.find_element_by_name('directory_name') # Find the search box
		elem.send_keys(employee_name + Keys.ENTER)
		# Have the program wait for 2 seconds for the javascript to laod
		time.sleep(2)   
		element = browser.find_element_by_xpath("//td[@data-label='NetID']")
		search = element.text
		# add to list
		unique_netID.append(search)
	except:
		# no person was found:
		unique_netID.append("")

##### Comments
# pretty good stuff, except you can get two people with just last name & first name: Robert Benoit

browser.quit()