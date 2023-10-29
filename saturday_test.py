# You are given a list of dictionaries, where each dictionary represents a book and contains information
# about its title, author, and a list of reviews, where each review is a dictionary containing information
# about the reviewer's name, rating, and comments. Write a function that takes in this list and returns the
# average rating for each book, along with the total number of reviews for each book. If a book has no
# reviews, its average rating should be 0.

input_list = [{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
               "reviews": [{"name": "John Doe", "rating": 4, "comments": "Great book!"},
                           {"name": "Jane Smith", "rating": 3, "comments": "Good read."},
                           {"name": "Bob Johnson", "rating": 5, "comments": "Amazing!"}, ]
               },
              {
                  "title": "To Kill a Mockingbird",
                  "author": "Harper Lee",
                  "reviews": [
                      {"name": "Alice Chen", "rating": 4, "comments": "Very well-written."},
                      {"name": "Tom Smith", "rating": 4, "comments": "Enjoyed reading it."},
                  ]
              },
              {
                  "title": "1984",
                  "author": "George Orwell",
                  "reviews": []
              }
              ]


def avg_reviews(input_list):
    # i am creating a fucntion name avg_reviews and took a parmeter input dictionary
    new_avg_rating_dict = {}
    # here i am creating an empty dictionary in which i store my output
    sum = 0
    # here i create a variable name sum which default value i gave '0'
    for i in input_list:
        # here  i am using for loop to access the list
        # print(i)
        # here i checked the list which was accessed by me but now its not a list it is now a dictionary
        for x in i['reviews']:
            # here i iterate for loop too get access in dictionary where i just want to access the reviews
            # print(value)
            rat = x['rating']
            # when i access the reviews then i need to get the access of rating and
            sum += rat
        #     here i am add the rating of books
        if(len(i['reviews']))>0:
            """ here i make a condition where i am getting the length and check the if reviews are greater then 
           zero then i have to get average of the reviews """
            avg = sum / len(i['reviews'])
            # here i took average of the reviews
            new_avg_rating_dict[i['title']] = {"average_rating":avg, "total_reviews":len(i['reviews'])}
        #     now here i put a empty dict beacuse i want to return the title and average rating and total reviews
        else:
            # else conditon if there is reviews are '0' or smaller then'0' then
            new_avg_rating_dict[i['title']] = {"average_rating":0, "total_reviews":0}
    #       here i want that which book had zero reviews which is also came in new dict
    return new_avg_rating_dict
# here i return the new _dictionary

y=avg_reviews(input_list=input_list)
# here i am the fucntion in a variable

print(y)
# now i am calling the function


# output
"""output - 

{
    "The Great Gatsby": {"average_rating": 4.0, "total_reviews": 3},
    "To Kill a Mockingbird": {"average_rating": 4.0, "total_reviews": 2},
    "1984": {"average_rating": 0, "total_reviews": 0}
}"""