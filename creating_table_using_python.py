def multiplication(x):
    for i in range(1, 11):
        table = (x, 'X', i, '=', x * i)
        print(table)
    return table


y = multiplication(9)
print(y)
