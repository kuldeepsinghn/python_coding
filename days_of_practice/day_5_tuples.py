#Q1 Create an empty tuple
empty_tuple = ()

# Q2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sister = ('sister1','sister2')
brothers = ('brother1','brother2')

#Q3 Join brothers and sisters tuples and assign it to siblings
siblings = (sister+brothers)


#Q4 How many siblings do you have?
len(siblings)

# Q5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('mother', 'father')
family_members = (siblings+parents)


# Q 6 Unpack siblings and parents from family_members
print("family_members:-",'mother', 'father')
print("siblings:-",'sister1','sister2','brother1', 'brother2'  )


# Q 7 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits =('banana', 'apple', 'papaya')
vegetables = ('potato', 'tomato', 'ladyfinger')
animal_product =('meat', 'chicken', 'beaf')

food_stuff_tp = (fruits+vegetables+animal_product)

#Q 8 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lst = list(food_stuff_tp)

# Q 9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item_tp = len(food_stuff_tp)//2
print(food_stuff_tp[middle_item_tp])

print(food_stuff_tp[0:])
print(food_stuff_lst[0:])

# Q 10 Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lst[0:4])
print(food_stuff_lst[-3:])

# Delete the food_staff_tp tuple completely

del(food_stuff_tp)

# Check if an item exists in tuple:

# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Iceland" in nordic_countries)
print("Estonia" in nordic_countries)

