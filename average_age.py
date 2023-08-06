students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

def average():
    values = students.values()
    age_sum = sum(values)
    print("Total age :", age_sum)
    # return sum(students) / len(students)
# print(average(students))
print(average())