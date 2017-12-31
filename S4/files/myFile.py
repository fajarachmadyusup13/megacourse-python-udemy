# file = open("fruits.txt", 'r')
# content = file.readlines()
# file.close()
# content = [ i.rstrip("\n") for i in content]
# print(content)

# for i in content:
#     print(len(i.rstrip("\n")))


# numbers = [1, 2, 3]
# file = open("myFile.txt", 'w')
# for i in numbers:
#     file.write(str(i)+"\n")
# file.close()


# temperatures=[10,-20,-289,100]
# def writer(temperatures):
#     with open("myFile.txt", "w") as file:
#         for t in temperatures:
#             if t > -273.15:
#                 f = t*9/5+32
#                 file.write(str(f)+"\n")
# writer(temperatures)

import glob2
import datetime

filenames = glob2.glob("*.txt")
now = datetime.datetime.now()

with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for i in filenames:
        with open(i, 'r') as f:
            file.write(f.read()+"\n")

