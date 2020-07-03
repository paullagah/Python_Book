# Hello World
def output():  # Defined a function called "output"
    return "Hello World!"  # Return "Hello World!" at the end of the function


print(output())  # print the result of the function

# Assignment
hello = "Hello World"


def output1(hello):     # Defined a function to called "output1"
    return hello         # Return the result of the function

print(output1(hello))

# Parameters
input1 = input("Please enter your input: ") # Asks for an input to be stored in the variable called "input1"


def output2(input1):                              # Defined a function called "output2"
    return input1                                 # Return the input given for "input1" at the end of the function


print(output2(input1))

# Parameters/Operators

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

def output3(num1, num2):
    return int(num1 + num2)

print("Answer is", output3(num1, num2))

# Conditionals

bool1 = input("Enter Boolean: ")
num3 = int(input("Please enter the first number: "))
num4 = int(input("Please enter the second number: "))

def output4(bool1, num3, num4):
    if bool1 == "True":
        return num3 + num4
    else:
        return num3 * num4

print(output4(bool1, num3, num4))


# Conditionals 2

