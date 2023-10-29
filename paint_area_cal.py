def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def get_even_numbers(numbers):
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
  return even_numbers

def get_even_numbers(numbers):
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
  return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)