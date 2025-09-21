# note -> 
# Return -> Return is used inside the function
# it end the function immediately and sends back the value to the caller
# After return, no further line inside the function are executed

# Recursion -> Same function calling itself is called as recursion 

# Recurision Function -> without stop/break condition
# In python the maximum recursion deapth is 1000
def increment_and_print(counter : int):
    counter = counter + 1
    print(f"{counter}")
    increment_and_print(counter)

#increment_and_print(0) 

# Recursion Function -> with stop/break condition 

def increment_and_print_1(counter : int):
    if (counter >= 10): #conditon declared at Beginning !
        return counter 
    counter = counter + 1
    print(f"{counter}")
    increment_and_print_1(counter)
    print(f"{counter}")

#increment_and_print_1(0)

# Recursion Fucntion -> with stop/break condition declared at last 

def increment_and_print_2(counter : int):
    counter = counter + 1
    print(f"{counter}")
    increment_and_print_2(counter)

    if (counter >= 10): # condition declared at last !
        return counter
    
#increment_and_print_2(0)

# When we declare the recursion condition in last in Python the recursion will reach maximum depth, therfore we should always write the break condition in the beginning 

#multiple - times calling of the recursion 
def increment_and_print_3(counter : int):
    if (counter >= 2): #conditon declared at Beginning !
        return counter 
    counter = counter + 1
    print(f"{counter}") # values pushed in the stack 
    increment_and_print_3(counter)
    print(f"{counter}") 
    increment_and_print_3(counter)
    print(f"{counter}")

increment_and_print_3(0) 



