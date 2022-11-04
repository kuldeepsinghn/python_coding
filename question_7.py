def function_2(students, x):
    new_dict = {}
    for p, q in students.items():
        # print(x, y)
        for a, b in q.items():
            # print(a, b)
            if x == b:
                new_dict[p] = b
    return new_dict
