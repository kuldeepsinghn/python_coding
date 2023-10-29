def test(flat_dict):
    return list(flat_dict.keys())


students = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
students.update({"ritu": 17})
print("students:", test(students))

keys = ["kuldeep", "ritu", "bitu", "rohit"]
values = [19, 17, 21, 18]
Name_error = dict(zip(keys, values))
print(Name_error)
Name_error["lucky"] = 15
print(Name_error)
