def myAge(age):
    new_age = age + 50
    return new_age

age = float(input("Enter your age: "))

if age > 150:
    print("How is that possible?")
else:
    print(myAge(age))
