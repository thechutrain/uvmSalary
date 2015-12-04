from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

# this function takes in the text file of employee names & netIds
# and searches the netIds with the with selenium


def getMoreInfo(yes_netId_txt):
    # extract_info takes in the html as a string, and returns
    # a list of the name, department, title, and primary affiliation
    def extract_info(html):
        # get the name
        name = re.search(r'Name:</span><span><p>(.*?)</p>', html, re.M | re.I)
        # print name.group(1)

        # get the department they are in
        department = re.search(
            r'Department:</span><span><p>(.*?)</p>', html, re.M | re.I)
        # print department.group(1)

        # get their title
        title = re.search(r'Title:</span><span><p>(.*?)</p>',
                          html, re.M | re.I)
        # print title.group(1)

        # get their primary affiliation
        primary_affiliation = re.search(
            r'Primary Affiliation:</span><span><p>(.*?)</p>', html, re.M | re.I)
        # print primary_affiliation.group(1)
        return_list = [name.group(1), department.group(1).replace(
            "&amp;", "&"), title.group(1), primary_affiliation.group(1)]
        return return_list

    ############## Get the employee name & netId ############
    # read each line in the text file
    text_file = open(yes_netId_txt, "r")
    name_netId_dict = {}
    for line in text_file:
        line_split = line.split("||")
        full_name = line_split[0]
        netId = line_split[1].rstrip('\n').lstrip(' ')
        # add full_name & netId to the dictionary
        name_netId_dict[full_name] = netId
    # pprint.pprint(name_netId_dict)

    ############## SELENIUM & Get to the page to get the html ###############
    browser = webdriver.Firefox()
    html_source = " "
    url_base = "http://www.uvm.edu/directorylisting/"
    for key in name_netId_dict:
        netId = name_netId_dict[key]
        # url is a combination of base + netId
        url = url_base + netId
        browser.get(url)
        html_source = browser.page_source
        soup = BeautifulSoup(html_source)
        summary = soup.find(id="directory_container")
        summary = str(summary)
        # Make two files; one if all data is there & other if data is not there
    	all_data = open("data/allData.txt", "a")
    	missing_data = open("data/missingData.txt", "a")
        try:
            info = extract_info(summary)
            # write to the allData file
            all_data.write(key)
            all_data.write("||")
            all_data.write(netId)
            all_data.write("||")
            all_data.write(info[0])
            all_data.write("||")
            all_data.write(info[1])
            all_data.write("||")
            all_data.write(info[2])
            all_data.write("||")
            all_data.write(info[3])
            all_data.write("\n")

        except:
        	# write to the missing data file
        	missing_data.write(key)
        	missing_data.write("||")
        	missing_data.write(netId)
        	missing_data.write("\n")
        #close file
        all_data.close()
        missing_data.close()

    browser.quit()


# call the function getMoreInfo
getMoreInfo("Yes_netId.txt")
