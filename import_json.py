import json
import pymysql


# Opening JSON file
def read_json():
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data.keys():
        subData = data[i]
        for element in subData.keys():
            print(element, subData[element])
            # print(i,data[i])

        # Closing file
    return f.close()


print(read_json())
