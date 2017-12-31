def celsius_to_fahrenheit(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        return (c*9/5)+32
    

c = float(input("insert celsius temperature: "))
print(celsius_to_fahrenheit(c))




# def check_size(myStr):
#     if type(myStr) == int:
#         return "Sorry Integers don't have length"
#     elif type(myStr) == float:
#         return "Sorry Floats don't have length"
#     else:
#         return len(myStr)    
    

# print(check_size(10.1))