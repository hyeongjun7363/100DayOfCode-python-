# TypeError
#print(len(123))

# type checking
print(type(123))
print(type("hello"))
print(type(3.14))
print(type(True))

# type conversion
print(int("123") + int("1234"))
#print(int("123") + int("abc")) -> type conversion error

# concatenate error
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# function - int, round
bmi = 84 / 1.65 ** 2
print(bmi)


print(int(bmi))

#round function
#round(number, digits)
print(round(bmi))
print(round(bmi, 2))

# assignment operator
a = 0
a += 1
print(a)

#f-string
is_winning = True
print(f"your bmi is {bmi}, and you are {is_winning}")
