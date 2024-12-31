height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print("Your bmi is " + str(bmi) + ".")

if bmi < 18.5:
    type = "underweight"
elif 18.5<= bmi < 25:
    type = "health body weight"
elif 25 <= bmi < 30:
    type = "overweight"
elif 30 <= bmi < 40:
    type = "obese"
else:
    type = "severely obese"
print("And you are " + type + ".")