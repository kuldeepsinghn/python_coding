""" Implement a function that receives the "ages" dictionary and a number "n" and returns a new dict where
 each student is (n) years older. For instance, new_ages(ages, 10) returns a copy of "ages" where each
 student is 10 years older."""
def function(ages,n):
    new_ages = {}
    for name, age in ages.items():
        # print(x, y)
        if age == n:
            # age == n => 10 == 10 true ya false

            new_ages[name] = age
    return new_ages



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
n=10

x= function(ages,n)
print(x)