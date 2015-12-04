

# this function takes in the text file of employee names & netIds
# and searches the netIds with the with selenium
def getMoreInfo(yes_netId_txt):
	# extract_info takes in the html as a string, and returns
	# a list of the name, department, title, and primary affiliation
	def extract_info(html):
		# get the name 
		name = re.search(r'Name:</span><span><p>(.*?)</p>', html, re.M|re.I)
		#print name.group(1)

		# get the department they are in
		department = re.search(r'Department:</span><span><p>(.*?)</p>', html, re.M|re.I)
		# print department.group(1)

		# get their title
		title = re.search(r'Title:</span><span><p>(.*?)</p>', html, re.M|re.I)
		#print title.group(1)

		# get their primary affiliation
		primary_affiliation = re.search(r'Primary Affiliation:</span><span><p>(.*?)</p>', html, re.M|re.I)
		#print primary_affiliation.group(1)
		return_list = [name.group(1), department.group(1).replace("&amp;", "&"), title.group(1), primary_affiliation.group(1)]
		return return_list
	############## Get the employee name & netId ############
	# read each line in the text file
	text_file = open(yes_netId_txt, "r")
	for line in text_file:
		line_split = line.split("||")
		full_name = line_split[0]
		netId = line_split[1].rstrip('\n').lstrip(' ')
		# print full_name
		# print netId



##### call the function getMoreInfo
getMoreInfo("Yes_netId.txt")