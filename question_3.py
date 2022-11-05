def oldest_person(ages):
    max_age = 0
    max_age_name= ' '
    for name, age in ages.items():
        print(name, age)
        if max_age_name is None or (age > max_age):
            max_age = age
            max_age_name= name
    return max_age, max_age_name
