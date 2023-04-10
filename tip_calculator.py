print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? $"))
tip= int(input("how much percentage u want to give a tip 10,12 or 15?"))
people= int(input("how many people have to split this bill?"))
tip_as_percent= tip/100
total_tip= bill*tip_as_percent
total_tip= tip/100 * bill+bill
total_bill = bill + total_tip
print(total_bill/people)
