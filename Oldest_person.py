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


def oldest_student():
    return max(ages, key=ages.get)


print("Oldest person in this student_dictionary is : ", oldest_student())


