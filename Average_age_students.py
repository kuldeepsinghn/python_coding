ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}


def average_age():
    values = ages.values()
    age_sum = sum(values)
    print("Total age :", age_sum)

    age_length = len(ages)
    print("length of total ages :" ,age_length)

    average = age_sum / age_length
    return average


print("The average of total age is :", average_age())
