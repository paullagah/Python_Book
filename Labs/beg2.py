hello = print("Hello World")        # Stored "Hello World" in a variable called "hello"


def output():                       # Defined a function to called "output"
    print(hello)                    # Print the stored variable
    return output()                 # Return the result of the function

