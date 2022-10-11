import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data.keys():
    subData = data[i]
    for ele in subData.keys() :
        print(ele,subData[ele])
    #print(i,data[i])


# Closing file
f.close()