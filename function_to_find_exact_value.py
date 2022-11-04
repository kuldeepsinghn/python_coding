def function(ages,n):
    new_ages = {}
    for name, age in ages.items():
        # print(x, y)
        if age == n:
            new_ages[name] = age
    return new_ages
