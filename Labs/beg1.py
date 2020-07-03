def output():  # Defined a function called "output"
    return "Hello World!"  # Return "Hello World!" at the end of the function


print(output())  # print the result of the function

hello = print("Hello World")  # Stored "Hello World" in a variable called "hello"


def output1():  # Defined a function to called "output1"
    print(hello)  # Print the stored variable
    return output1()  # Return the result of the function


input1 = input("Please enter your input: ") # Asks for an input to be stored in the variable called "input1"


def output2():                              # Defined a function called "output2"
    return input1                           # Return the input given for "input1" at the end of the function


print(output2())
