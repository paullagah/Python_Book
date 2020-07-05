# # Hello World
# def output():  # Defined a function called "output"
#     return "Hello World!"  # Return "Hello World!" at the end of the function
#
#
# print(output())  # print the result of the function
#
# # Assignment
# hello = "Hello World"
#
#
# def output1(hello):     # Defined a function to called "output1"
#     return hello         # Return the result of the function
#
# print(output1(hello))
#
# # Parameters
# input1 = input("Please enter your input: ") # Asks for an input to be stored in the variable called "input1"
#
#
# def output2(input1):                              # Defined a function called "output2"
#     return input1                                 # Return the input given for "input1" at the end of the function
#
#
# print(output2(input1))
#
# # Parameters/Operators
#
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
#
# def output3(num1, num2):
#     return int(num1 + num2)
#
# print("Answer is", output3(num1, num2))
#
# # Conditionals
#
# bool1 = input("Enter Boolean: ")
# num3 = int(input("Please enter the first number: "))
# num4 = int(input("Please enter the second number: "))
#
# def output4(bool1, num3, num4):
#     if bool1 == "True":
#         return num3 + num4
#     else:
#         return num3 * num4
#
# print(output4(bool1, num3, num4))
#
#
# # Conditionals 2
#
# bool2 = input("Enter Boolean: ")
# num5 = int(input("Please enter the first number: "))
# num6 = int(input("Please enter the second number: "))
#
#
# def output5(bool2, num5, num6):
#     if num5 == 0:
#         return num6
#     elif num6 == 0:
#         return num5
#     elif bool2 == "True":
#         return num5 + num6
#     else:
#         return num5 * num6
#
#
# print(output5(bool2, num5, num6))
#
# # Recursion
# loop = []
#
#
# def output6():
#     for i in range(10):
#         loop.append(output5(bool2, num5, num6))
#     return loop
#
#
# print(output6())
#
# # Lists
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def output7(l1):
    return l1[0]

print(output7(l1))

# Recursion/Lists

def output8(l1):
    for i in range(10):
        return l1[::1]

print(output8(l1))

# Recursion/Lists 1
l2 = []

def output9(l2):
    count = 0
    while count < 10:
        l2.append(int(input("Give a number please: ")))
        count += 1
    for i in range(10):
        return l2 * 10

print(output9(l2))