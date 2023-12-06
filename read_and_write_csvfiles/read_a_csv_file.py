# import csv
#
# # Input and output file paths
# input_file = 'D:\\git_hub\\python_\\python_coding\\markdown_files\\rajasthan_user_data.csv'
# output_file = 'D:\\git_hub\\python_\\python_coding\\markdown_files\\rajasthan_user_data_heightsincm.csv'
#
# # Define the heights for each person
# height_data = [
#     {'name': 'Kuldeep', 'height': 175},
#     {'name': 'Kamal', 'height': 180},
#     {'name': 'Ajay', 'height': 165},  # Provide a default value for missing height
# ]
#
# # Create a dictionary to map names to heights
# name_to_height = {item['name']: item['height'] for item in height_data}
#
# Open the input and output CSV files
# with open(input_file, 'r') as read_file, open(output_file, 'w', newline='') as write_file:
#     csv_reader = csv.reader(read_file)
#     csv_writer = csv.writer(write_file)
#
#     # Read the header row from the input file
#     header = next(csv_reader)
#
#     # Add "height" to the header row
#     header.append("height")
#     csv_writer.writerow(header)
#
#     # Iterate through the rows, add the "height" column based on the name, and write the updated rows
#     for row in csv_reader:
#         name = row[0].strip()  # Make names lowercase for case-insensitive matching
#         height = name_to_height.get(name, '')  # Get the height based on the name
#         row.append(height)
#         csv_writer.writerow(row)


import csv
import json


def read_csv_file(file_path):
    data = []#empty list

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        print(reader)
        header = next(reader)

        for row in reader:
            # print(row)
            # Create a dictionary for each row by pairing column names with row values
            row_dict = {}
            for key, value in enumerate(row):
                # print(key)
                # print(value)
                column_name = header[key]
                row_dict[column_name] = value

            username= row_dict.get('Username','')
            row_dict['length']=len(username)
            data.append(row_dict)

    return data


# Usage example
file_path = 'D:\\git_hub\\python_\\python_coding\\markdown_files\\rajasthan_user_data.csv'
csv_data = read_csv_file(file_path)
print(csv_data)

json_file_path = 'rajasthan_user_data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(csv_data, json_file)
