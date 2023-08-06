def common_number(lis, list1):
    for i in lis:
        for j in list1:
            if i == j:
                result = True
    return result


x = common_number(lis=[11, 2, 3, 4, 5, 6, 7, 8, 9], list1=[11, 21, 12, 34, 45, 56, 78, 98, 65])
print(x)