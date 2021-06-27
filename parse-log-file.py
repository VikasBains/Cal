# Getting Started
# Attached is a compressed log file. Extract it and have a quick look at the format.

# Now, write a command line tool that parses the log and presents the following info to the user:

#   What are the number of requests served by day?
#   What are the 3 most frequent User Agents by day?
#   What is the ratio of GET's to POST's by OS by day?

# Guidelines
# Use the following tools:

#   GitHub
#   Java or Python
#   Your favorite editor
# Organize the project as you would normally structure a production-ready tool.

# Ship it
# Once you’re done, send us a link to your GitHub repo. We’ll review based on:
#   Code quality
#   Best­ practices
#   Testing
#   Design
#   Style

# Bonus Points
#   Add command line switches (e.g., verbose mode)
#   Provide a help screen
#   Provide sufficient test coverage

##############################
# Solution 1
##############################

# taking a variable and opening the log file in it.
file_handle = open('sample.log','r')
# initializing a dictionary to create histogram for the count of requests by date.
counts = dict()
# initializing a list to get the dates.
dates = []

# loop to get the dates.
for line in file_handle:
  lines = line.split()
  date_format = lines[3].split(':')[0].strip('[')
  dates.append(date_format)

# loop to create dictionary.
for i in dates:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

# printing out the dictionary which tells the count.
# print(counts)
# print('-- OR --')
print('Number of queries per day:')
for k,v in counts.items():
  print(k,v)

print()
##############################
# Solution 2
##############################

file_handle = open('sample.log')
counts = dict()
# considering agent is specified in column number 11, and initializing a list to store all of them.
agents = []

# loop to get the list of agents.
for line in file_handle:
  lines = line.split()
  agent_name_format = lines[11].split('/') 
  agent_name_format = agent_name_format[0].split('+')
  agent_name_format = agent_name_format[0].split('(') 
  agent_name_format = agent_name_format[0].strip('"|;|\\|_')
  agents.append(agent_name_format)

# creating dictionary of agents.
for i in agents:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

# print(counts)
# To Sort the dictionary by value
# initialize a list to get all the values (agent names and occurance) in a list.
lst = list()

# loop to insert dict values in a list.
for key, val in list(counts.items()):
    lst.append((val, key))

# reverse sorting the list.
lst.sort(reverse=True)

print('Top 3 agents and their count:')
# loop to print the top 3 agents.
for key, val in lst[:3]:
    print(key, val)

print()
##############################
# Solution 3
##############################
import re

# function to get the number of GET and POST for all the lines which has 'Linux' in it.
def get_post_linux():
    file_handle = open('sample.log')
    # initialize counter for GET and POST requests.
    count_linux_get = 0
    count_linux_post = 0
    for line in file_handle:
        # getting the string inside paranthesis, becuase that is where OS is. mentioned.
        # save the result in vaiable 'res'
        res = re.findall(r'\(.*?\)', line)
        # print(res)
        for i in res:   
            # look for word 'Linux' in above result.
            if 'Linux' in i:
                # increment the counter if GET or POST.
                if 'GET' in line:
                    count_linux_get += 1
                elif 'POST' in line:
                    count_linux_post += 1
    print('GET calls for Linux =', count_linux_get)
    print('POST calls for Linux =', count_linux_post)

# Similarily.
# function to get the number of GET and POST for all the lines which has 'Windows' in it.
def get_post_win():
    file_handle = open('sample.log')
    count_win_get = 0
    count_win_post = 0
    for line in file_handle:
        res = re.findall(r'\(.*?\)', line)
        #print(res)
        for i in res:   
            if 'Windows' in i:
                if 'GET' in line:
                    count_win_get += 1
                elif 'POST' in line:
                    count_win_post += 1
    print('GET calls for Windows =', count_win_get)
    print('POST calls for Windows =', count_win_post)

# def get_ratio():
#     file_handle = open('sample.log','r')
#     counts = dict()
#     dates = []

#     for line in file_handle:
#         lines = line.split()
#         date_format = lines[3].split(':')[0].strip('[')
#         dates.append(date_format)
                
#     for i in dates:
#         if i not in counts:
#             counts[i] = 1
#         else:
#             counts[i] += 1

    # print(counts)
    # print('-- OR --')
    # for k,v in counts.items():
    #     print(k,v)

    # uniq_dates = list(set(dates))
    

###### Output ########
print('Ratio of GET and POST requests by OS type:')
get_post_linux()
print()
get_post_win()
# get_ratio()
