def square_of_elements(input_list):
    new_list = []
    for elements in input_list:
        new_list.append(elements ** 2)

    return new_list


output = square_of_elements([25])
print(f"the square of elements of a list are{output}")


def cube_elements(input_list):
    new_list = []
    for i in input_list:
        new_list.append(i * i * i)
    return new_list


result = cube_elements([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)


def multiplication(x):
    table = 0
    for i in range(1, 11):
        table = (x * i)

    return table


result = multiplication(5)
print(result)
