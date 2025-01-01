print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip_persent = int(input("How much tip would tou like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

pay_with_bill = total_bill * (1 + tip_persent / 100)
personal_pay = pay_with_bill/ people
print(f"Each person should pay: ${round(personal_pay,2)}")
