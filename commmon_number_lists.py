def common_number(lis, list1):
    common_list =[]
    for i in lis:
        for j in list1:
            if i == j:
                common_list.append(i)
                result = True
    return result, common_list


x,p= common_number(lis=[11, 2, 34, 45, 5, 6, 7, 8, 9], list1=[11, 21, 12, 34, 45, 56, 78, 98, 65])
print(p)