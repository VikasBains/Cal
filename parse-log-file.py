# Getting Started
# Attached is a compressed log file. Extract it and have a quick look at the format.

# Now, write a command line tool that parses the log and presents the following info to the user:

# 	What are the number of requests served by day?
# 	What are the 3 most frequent User Agents by day?
# 	What is the ratio of GET's to POST's by OS by day?

# Guidelines
# Use the following tools:

# 	GitHub
# 	Java or Python
# 	Your favorite editor
# Organize the project as you would normally structure a production-ready tool.

# Ship it
# Once you’re done, send us a link to your GitHub repo. We’ll review based on:
# 	Code quality
# 	Best­ practices
# 	Testing
# 	Design
# 	Style

# Bonus Points
# 	Add command line switches (e.g., verbose mode)
# 	Provide a help screen
# 	Provide sufficient test coverage

##############################
# Solution
##############################

# file_handle = open('sample.log','r')
# counts = dict()
# dates = []

# for line in file_handle:
# 	lines = line.split()
# 	date_format = lines[3].split(':')[0].strip('[')
# 	dates.append(date_format)


# for i in dates:
#     if i not in counts:
#         counts[i] = 1
#     else:
#         counts[i] += 1

# print(counts)
# print('-- OR --')
# for k,v in counts.items():
# 	print(k,v)
########################

# file_handle = open('sample.log')
# counts = dict()
# considering agent is specified in column number 11
# agents = []

# for line in file_handle:
# 	lines = line.split()
# 	agent_name_format = lines[11].split('/') 
# 	agent_name_format = agent_name_format[0].split('+')
# 	agent_name_format = agent_name_format[0].split('(') 
# 	agent_name_format = agent_name_format[0].strip('"|;|\\|_')
# 	agents.append(agent_name_format)

# for i in agents:
#     if i not in counts:
#         counts[i] = 1
#     else:
#         counts[i] += 1

# # print(counts)

# # Sort the dictionary by value
# lst = list()

# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)

# for key, val in lst[:3]:
#     print(key, val)

##########################################

# import re
# file_handle = open('sample.log')

# for line in file_handle:
# 	res = re.findall(r'\(.*?\)', line)
# 	#print((res))
# 	for i in res:	
# 		if i is not None:
# 			os = i.split(';')
# 			for name in os:
# 				if (('Windows') or ('Linux')) in name:
# 					print(name)

import re

file_handle = open('sample.txt','r')
counts = dict()
dates = []

for line in file_handle:
	lines = line.split()
	date_format = lines[3].split(':')[0].strip('[')
	dates.append(date_format)
	so = re.match(r"(.*)" ,line).groups()
	print(so)

for i in dates:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

# for k,v in counts.items():
# 	print(k,v)


