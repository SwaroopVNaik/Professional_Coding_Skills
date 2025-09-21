# ------------------------ Coding Workshop - 1 --------------------------------------------------------------!

# Question - 1 : Function to getSum of two numbers ?
# Solution_1 : Method_1 ->
# Function Definition 👇
def getSum(number_1 : int, number_2 : int ) -> int: # <- Function Declaration
    sum = number_1 + number_2
    print(sum)

# Function Invocation / Calling  -> 
getSum(10, 10)

# Solution_1 : Method_2 -> 

# Function Definition 👇
def total_of_Numbers(num_1 : int, num_2 :int) -> int: # <- Function Declaration
    return ( num_1 + num_2 )

# Function Invocation / Calling  -> 
total = total_of_Numbers(24 , 7)
print(total)
#------------------------------------------------------------------------------------------------------------!
# Question - 2 : Function SwapNumbers to Swap two variable Values ?
# Solution_2 : Method -> 1
# Function Definiton 👇
def SwapNumbers(Var_1_Value: int, Var_2_Value: int): # <- Function Declaration
    temp = Var_1_Value
    Var_1_Value = Var_2_Value
    Var_2_Value = temp
    
    # Return both values back. 
    # Python automatically packs them into a tuple (Var_1_Value, Var_2_Value)
    return Var_1_Value, Var_2_Value


# Function Invocation / Calling ->
Value_A = 7
Value_B = 24

print(f"Before Swapping: Value_A = {Value_A}, Value_B = {Value_B}")

# Here, SwapNumbers returns a tuple like (24, 7).
# Python unpacks it and assigns Value_A = 24, Value_B = 7.
Value_A, Value_B = SwapNumbers(Value_A, Value_B)

print(f"After Swapping: Value_A = {Value_A}, Value_B = {Value_B}")

# Solution_2 : Method -> 2
# Function Definiton 👇
def SwapNumbers_2(Var1 : int, Var2 : int): # <- Function Declaration
    return Var2, Var1

# Function Invocation / Calling ->
Num1 = 24
Num2 = 26

print(f" Before Swapping : Num1 = {Num1} and Num2 = {Num2} ")

Num1 , Num2 = SwapNumbers_2(Num1, Num2)

print(f" Before Swapping : Num1 = {Num1} and Num2 = {Num2} ")
#------------------------------------------------------------------------------------------------------------!
# Question - 3 : Function isEven to return true if numbers is even otherwise false :
# Solution_3 : Method -> 1
# Function Definition 👇 
def isEven(Number : int) ->int: # <- Function Declaration
    if(Number % 2 == 0):
        print(f" Number = {Number} is Even ! ")
    else:
        print(f" Number = {Number} is Odd ! ")
    return Number

# Function Invocation / Calling ->

FindoutEvenOrOdd = isEven(3)

#Solution_3 : Method -> 2 ( Using boolean )
# Function Definition 👇 
def isEven_2(Num : int) -> bool: # <- Function Declaration
    if(Num % 2 == 0):
        return True
    else:
        return False

# Function Invocation / Calling  
user_input = 10
FindoutEvenOrOdd_2 = isEven_2(user_input)
if(FindoutEvenOrOdd_2):
    print(f" The Number = {user_input} is Even ")
else:
    print(f" The Number = {user_input} is Odd ")
#------------------------------------------------------------------------------------------------------------!
# Question - 4 :  Write a Function isdigit / isNumber to return true if it is a digit(Number) :
# solution_4 : Method -> 1
# Function Definition 👇
def isDigit(Numbers : str) -> bool: # <- Function Declaration 
    isInteger = True #Flagging ( Assuming that everything is Integer )

    for eachcharacter in Numbers:
        if(eachcharacter >= '0' and eachcharacter <= '9' ):
            continue
        else:
            isInteger = False
            break
    return isInteger

# Function Invocation / Calling
RESULT = isDigit("12a34")
if(RESULT):
    print(" The Value is a Digit ")
else:
    print(" The Value is not a Digit ")

# Solution_4 : Method -> 2 
# Function Definition 👇

def isDigit_2(Num3 : str) -> bool: # <- Function Declaration
    for eachChar in Num3:
        #check if any character falls outside the range 0 to 9, if yes return False
        if(eachChar < '0' or eachChar > '9'):
            return False # here we are trying to do early exit by declaring wrong conditon for it to exit soon !
        
        #If no charcters falls outisde the range 0 to 9 , return True 
    return True

# Function Invocation / calling 
RESULT_2 = "2407"
checkisDigitYesorNO =isDigit_2(RESULT_2)
if(RESULT_2):
    print(f" The Value is a Digit ")
else:
    print(f" The Value is not a Digit ")

#--------------------------------------------------------------------------------------------------------------!
# Question 5 : Function SimpleGreeting to accept name as input and print Simple Greetings Namaskara Name
# Solution_5 : ->
# Function definiton 👇
def simpleGreetings(): # <- Function Declaration
    name = input(" Enter your Name : ")
    age = input( "Enter your age : ")

    print(f" Namaskara {name}")
    print(f"your age is = {age}")

#Function Invocation / calling 
simpleGreetings()

#-------------------------------------------Coding Workshop - 2------------------------------------------------!
# Question 6 : Function to print ASCII Values of String Input 
# Solution_6 : ->
# Function definiton 👇
def ASCII_Values_str(string): # <- Function Declaration
    for charcaters in string:
        Value_ascii = ord(charcaters) #ord() Function to find ASCII value of Character ! 
        print(f"The ASCII Values of {charcaters} is {Value_ascii} ")

#Function Invocation / calling 
ASCII_Values_str("A")
#-------------------------------------------------------------------------------------------------------------!
# Question 7 : Function StrLength to get String Length
# Solution_7 : ->
# Function definiton 👇
def StrLength(string : str, ) -> int: # <- Function Declaration
    counter = 0
    if string is not None: #( != in python instead of using (not Equal) operators we can also use (is Not))
        for character in string:
            counter = counter + 1
    return counter

#Function Invocation / calling 
input_1 = None # NUll (No container)
print(f"The String Length of {input_1} is : {StrLength(input_1)}")

input_2 = "" #Empty String (No item inside container)
print(f"The String Lenght of {input_2} is : {StrLength(input_2)}")

input_3 = "s" #One item in the String ( one item inside the container )
print(f"The String Length of {input_3} is : {StrLength(input_3)}")

input_4 = "swaroop" #Many items items in string (contianer filled with items)
print(f"The String Length of {input_4} is : {StrLength(input_4)}")
#-----------------------------------------------------------------------------------------------------------!
# Question 8 : Function to CountVowels get of vowel of a given String
# Solution_8 : ->
# Function definiton 👇
def Count_Vowels(String : str) -> int: # <- Function Declaration
    counter = 0
    if String is not None: #( != in python instead of using not Equal operators we can also use (is Not))
        for character in String:
            if (character == 'a' or  
                character == 'e' or 
                character == 'i' or  
                character == 'A' or 
                character == 'u' or  
                character == 'E' or  
                character == 'o' or  
                character == 'I' or
                character == 'O' or  
                character == 'U'):
                counter = counter + 1
    return counter

#Function Invocation / calling 
#input = None -> the input user giving to string ( input parameter ) of the function.
print(f"Number of Vowels {None} in  = {Count_Vowels(None)}")

#input = "" -> the input user giving to string ( input parameter ) of the function.
print(f"Number of Vowels {""} is = {Count_Vowels("")}")

#input = "S" -> the input user giving to string ( input parameter ) of the function.
print(f"Number of Vowels {"S"} is = {Count_Vowels("S")}")

#input = "Swaroop" -> the input user giving to string ( input parameter ) of the function.
print(f"Number of Vowels {"Swaroop"} is = {Count_Vowels("Swaroop")}")
#------------------------------------------------------------------------------------------------------------!
# Question 9 : Function to ReverseString Reverse String 
#Iterater -> if there is series of numbers fetching each element one by one is called iterater
# Solution 9 : ->
# Function definiton 👇
def reverseString(string : str): # -> Function Declaration
    length = len(string)
    middle = int(length/2) #typecasting - to converts decimal (float) value to integer value we use typecasting.

    print(f"length = {length}")
    print(f"middle = {middle}")

    #range(0, length , 1) 
    # -> 0 = strating point, length = stoping point -> length of the string (ex: 5 -> 0, 1, 2, 3, 4) , 1 -> step !
    #range(length - 1, - 1, - 1) 
    # -> Length - 1 Starting point (goes backward 5 -> 4, 3, 2, 1, 0), -1 -> last valid number 0, -1 
    # -> deacrses each step -1 to go backward
    # ZIP () Function -> takes number from first range and end and pairs them 
    # ZIP () example -> (0, 4), (1, 3), (2, 2) (3, 1), (4, 0) 
    # element 1 = Start - Range; element 2 = End - Range

    #for start, end in zip(range(0, length, 1), range(length - 1, - 1, - 1)):
    #print(f"Start : {start}, end : {end}") #prints the paired element of first range and end Range
    #Swapping the Characters 
    #string[start], string[end] = string[end], string[start]

    reverseString = "" #Empty String to store the Reversed String
    for end in range(length - 1, - 1, - 1):
       
        #length - 1 → last index of string. If string has 7 chars, last index = 6.
        #-1 → stopping point (loop will stop before -1, so last index processed is 0).
        #-1 → step value (means go backwards, decrementing by 1).
        #👉 So, loop runs from last character → first character.

        reverseString += string[end]

        #Take each character from the (end) and keep adding to -> reverseString.

    return reverseString  #Returning the Reverse String

# Function invocation / calling ->
name = "Swaroop"
name = reverseString(name)
print(name)
#---------------------------------------------------------------------------------------------------------------------------------------!
# Question 10 : Function to get Sum of all elements in the integer arrray getSum
# Solution_10 : -> 
# Function definiton 👇
def getSum_Array(Numbers : list) -> int: # <- Function Declaration
    sum = 0

    for number in Numbers:
        sum = sum + number
    return sum

# Function invocation / calling ->
Numbers = [1, 2, 3, 4, 5]
SumOfNumbers = getSum_Array(Numbers)
print(f"Sum of numbers is = {SumOfNumbers}")  
#-------------------------------------------------Coding Workshop - 3-------------------------------------------------------------------!
# Question 11 : Function to find given string is Palindrome function, function isPalindrome returns true if string is Palindrome
# Solution_11 : ->
# Function Definition 👇 ->
def isPalindrome(string:str) -> bool: # <- Function Declaration
    leftIndex = 0 # left index - track
    RightIndex = len(string) - 1 # Right index - track
    result = True # Assuming String is palindrome

    while(leftIndex < RightIndex):
        if string[leftIndex] != string[RightIndex]:
            result = False
            break

        leftIndex += 1
        RightIndex -= 1
    return result


# Function Invocation / Declaration ->
IN_1 = "racecar"
IN_2 = "RaceCar"
IN_3 = "wasitacaroracatisaw"  
IN_4 = "python"
IN_5 = "palindrome"
IN_6 = "abxcba"
result = isPalindrome(IN_6)

if result:
    print(" String is palindrome ")
else:
    print(" String is not Palindrome ") 
#--------------------------------------------------------------------------------------------------------------------------------------!
# Question 12 : -> Function to print max and min value from an integer array, PrintMaxMin (Linear Search)
# Solution_12 : -> 
# Function Definition 👇 ->
def PrintMaxMin(array: list) -> tuple[int, int]: # <- Function Declaration
    max = array[0]
    min = array[0]

    for index in range(1, len(array), 1):
        if array[index] > max:
            max = array[index]

        if array[index] < min:
            min = array[index]

    return max, min

IPT_1 = [1, 5, 6, 8, 9]
resultMax, resultMin = PrintMaxMin(IPT_1)

print(f"Maximum Value is {resultMax} and the Minimum Value is {resultMin}") 
#---------------------------------------------------------------------------------------------------------------------------------------!
# Question 13 : -> Function to search in sorted integer array ( aka = Binary Search)
# divide and conquer technique
# solution_13 : -> 
#Function Definition 👇 ->
def search(NUMBERS , key) -> bool: # <- Function Declaration
    left_Index = 0
    right_Index = len(NUMBERS) - 1 
    found = False
    
    while(left_Index <= right_Index): 
        middle_Index = int(left_Index + (right_Index - left_Index) / 2) #Typecasting - Converting to Integer 

        if(NUMBERS [middle_Index] == key) :
            found = True
            break

        if(NUMBERS [middle_Index] > key):
            # you must search on the left side of the array
            right_Index = middle_Index - 1
        else:
            # we must search on the right side of the array
            left_Index = middle_Index + 1

    return found

# Function Invocation / Calling
IN_7 = [1, 2, 3, 4, 5, 6, 7]
key = 6

result_3 = search(IN_7, key)
if result_3:
    print(f" Result is found ! ")
else:
    print(" Number is not found ! ")  
#------------------------------------------------Coding - Workshop - 4-------------------------------------------------------------------!
# Question 14 : -> Functiont to merge two arrays and return combined output in first array 
# Solution_14 : -> 
# Function Definition 👇
def mergeList(List_1: list, List_2: list):# <- Function declaration
    for item in List_2:
        List_1.append(item) # append -> add the items at the end of the List_1
    #return list

# function invocation / calling
List1 = [1, 2, 3]
List2 = [4, 5]

mergeList(List1, List2) #dynamic memory allocation 
print(List1)
#---------------------------------------------------------------------------------------------------------------------------------------!
# Question 15 : ->  Function get second largest element in an array integer array getSecondLargest
# Solution_15 : -> 
# Function Definition 👇
def getSecondLargestMumber(Array_1 : int) -> int: # <- Function declaration
    largestMax = Array_1[0]
    Secondlargest = Array_1[0]

    for Index in range(1, len(Array_1), 1):
        #if the new number we scan is greater then cuurent largest
        # we have to update both variables 
        if(Array_1[Index] > largestMax):
            Secondlargest = largestMax
            largestMax = Array_1[Index]
        
        elif Array_1[Index] > Secondlargest and Array_1[Index] != Secondlargest:
            Secondlargest = Array_1[Index]
        elif largestMax == Secondlargest and Array_1[Index] < largestMax:
            Secondlargest = Array_1[Index]

    return Secondlargest

# Function Invocation / Calling 
IN_8 = [1, 2, 3, 4, 5]
result_4 = getSecondLargestMumber(IN_8)
print(f"The Second Largest Element is {result_4}")
#----------------------------------------------------------------------------------------------------------------------------------------!
# Method 2 -> Solution_15 : ->
# Function Definiton 👇
def getSecondLargestNumber_V2(array_2 :int) -> int: # <- Function declaration
    largestMax_V2 = float("-inf") # Setting integer value to minimum Value in Python !
    Secondlargest_V2 = float('-inf') # Setting integer value to minimum Value in Python ! 
    for Index_V2 in range(0, len(array_2), 1):
        #if the new number we scan is greater then cuurent largest
        # we have to update both variables 
        if(array_2[Index_V2] > largestMax_V2):
            Secondlargest_V2 = largestMax_V2
            largestMax_V2 = array_2[Index_V2]
        
        elif array_2[Index_V2] > Secondlargest_V2:
            Secondlargest_V2 = array_2[Index_V2]

    return Secondlargest_V2

# Function Invocation / Calling 
IN_9 = [5, 1, 2, 3, 4] #Values
IN_9 = [-1, -2, -3, -4, -5] #Values
result_5 = getSecondLargestMumber(IN_9)
print(f"The Second Largest Element is {result_5}")
#---------------------------------------------------------Coding Workshop - 5------------------------------------------------------------!
#Question 16 : -> Function to print unique elements in an integer array PrintUniqueElements 
#Solution_16 : ->
#Ignore those numbers completely which have duplicate
def PrintUniqueElements(NUM_A : int):
    for read_index in range(0, len(NUM_A), 1):
        isDuplicate = False #FLag 

        for compare_index in range(0, len(NUM_A), 1):
            if read_index == compare_index:
                continue
            
            if NUM_A[read_index] == NUM_A[compare_index]:
                isDuplicate = True
                break
            
        if(isDuplicate == False):
            # This is a unique element, hence print it
            print(NUM_A[read_index])

# Function Invocation/Calling 
IN_10 = [1,2, 3, 2, 4]
IN_11 = [1, 2, 3, 4, 5]
PrintUniqueElements(IN_10)
#----------------------------------------------------------------------------------------------------------------------------------------!
# Question 17 : -> Function to print intersection or common elements of two integer arrays getCommonElements
# Solution_17 : -> 
def getCommonElements(input_1 :list, input_2 : list):
    for input1_index in range(0, len(input_1), 1):
        isFound = False

        for input2_index in range(0, len(input_2), 1):
            if input_1[input1_index] == input_2[input2_index]:
                isFound = True
                break

        if  isFound:
            print(input_1[input1_index])

# Function Invocation/Calling 
IN_12= [1, 2, 3, 4 ,5]
IN_13 = [1, 2, 7, 4, 5]

getCommonElements(IN_12, IN_13)
#----------------------------------------------------------------------------------------------------------------------------------------!
# Question 18 : -> Function to get Count of Words in String getCountofWords 
# Solution_18 : -> 
# This code will work for no word or atleast no word 
def getCountofWords(string : str) -> int:
    counter = 1

    if(len(string) == 0):
        return 0

    for character in string:

        if character == ' ' or '\t' or character == '\n':
            counter = counter + 1

        #Special Case with just one word 
        if (len(string) > 0 and counter == 0):
            return 1
        
        return counter

IN_14 = "Hello World"
count = getCountofWords(IN_14)
print(f"Count of words = {count}")
#----------------------------------------------------------------------------------------------------------------------------------------!
# Question 19 : -> Function to print Binary Values of Various input like integer , char , also peform shift operations.
# Solution_19 : -> 
def printBinaryform(number : int):
    no_of_bits = number.bit_length()
    print(f"Number of bits = {no_of_bits}")

    mask = 1
    mask = mask << no_of_bits - 1

    for _ in range(no_of_bits):
        if(number & mask):
            print("1", end = " ") # end = " " to print in same line in pythob
        else:
            print('0', end = " ")

        mask = mask >> 1
              
# Function Invocation / Calling
printBinaryform(5)
printBinaryform(1024)
printBinaryform(102018)
#----------------------------------------------------------------------------------------------------------------------------------------!
# Question 20 : -> Function to remove the spaces from the string removeSpaces 
# Solution_20 : -> #In Python as we know we cannot chnages the values of string as it immutable 

def removeSpacesString(String : str):
    output  = ""

    for char in String:
        if char != ' ' and char != '\t' and char != '\n':
            output = output + char
    
    print(output)

#Function Invokacation/ Calling 
IN_15 = "I Am Swaroop        "
removeSpacesString(IN_15)
#----------------------------------------------------------------------------------------------------------------------------------------!
