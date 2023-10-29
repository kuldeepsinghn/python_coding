def BodyMassIndex():
    height= input("Please enter your height here in meter:-")
    weight= input("Please enter your weight here in kilograms:-")

    # BMI stands for body mass index which is used to check that our body fatness or we are healthy or not

    bmi= int(weight)/float(height)**2
    return bmi

x= BodyMassIndex()
print(x)