# import requests
#
# response = requests.get("https://img.freepik.com/premium-photo/wallpaper-with-tropical-leaves-red-blue-background_81048-4907.jpg?w=2000")
#
# # print(response.content)
# fp = open('wallpaper.png',"wb")
# fp.write(response.content)
# fp.close()
def generate_output():
    return "This is the output of my function."

# Open a new file for writing
with open('output.txt', 'w') as file:
    output = generate_output()  # Call your function to generate the output
    file.write(output)  # Write the output to the file
