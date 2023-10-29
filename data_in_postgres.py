"""Q - write a python function that takes one input which json file , read that file and insert into postgres table"""

import this_dict

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data.keys():
    subData = data[i]
    for element in subData.keys() :
        print(element,subData[element])
    #print(i,data[i])


# Closing file
f.close()