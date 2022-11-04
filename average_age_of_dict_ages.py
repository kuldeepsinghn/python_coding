def average_num(input_dictionary):
    print("input is this", input_dictionary)
    input_dictionary['xx'] = 11
    total = 0
    for i in input_dictionary.values():
        total += i

    avg_val = total / len(input_dictionary)
    return avg_val
