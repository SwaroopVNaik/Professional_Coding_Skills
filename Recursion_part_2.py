# Example :-> 1) Printing before and after recursive call 

#Function Declaration
def print_number_recursion(size: int):

    #Termination
    if (size == 0):
        return
    
    # Work or logic Block
    size = size - 1
    print("\n Before the Recursive Call : ", size)

    # Recursive Call
    print_number_recursion(size)
    # This code is removed after function is removed from the stack
    print("\n After the recursive call : " , size)


# Invocation Function
print_number_recursion(5)

# Example :-> 2)  Multiple Recursive Call ( fibonnaci )

# Function Declaration 
def Fibonnaci(number : int):

    #  Base Case (stopping condition for recursion)
    print("Recursive Function invoked with the number", number)
    if(number <= 1):
        return number

    print("First recursive call is getting invoked")

    # Recursive Call - 1
    result_1 = Fibonnaci(number - 1)
    print("Result_1 value = ", result_1)

    print("Second recursive call is getting invoked")

    # Recursive Call - 2
    result_2 = Fibonnaci(number - 2)
    print("Result_2 Value = ", result_2)
    
    # Combine the results of the two recursive calls
    answer = result_1 + result_2
    print("Answer Value = ", answer)

    return answer

# Function invocation
result = Fibonnaci(5)
print("Result is " , result)

