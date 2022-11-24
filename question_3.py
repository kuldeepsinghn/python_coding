# Implement a function that receives the "ages" dictionary as parameter and returns the name of the oldest student.
def oldest_person(ages):
    max_age = 0  # max age find krne k liye
    max_age_name = None  # max age wale bande ka  naaam find krne k liye

    for name, age in ages.items():  # name = key , age = values
        # print(name, age)

        if age > max_age:  # condition
            max_age = age
            max_age_name = name
    return max_age_name, max_age


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
oldest_person_name = oldest_person((ages))
print(oldest_person_name)
