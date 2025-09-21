# Example_1 : Is Number Positive ->
# if statement :
Number = 10

if (Number > 0):
    print(" Number is Positive ! ")

# if - else statement :
Number_1 = - 24

if (Number_1 > 0):
    print(" Number_1 is Positive ! ")
else:
    print(" Number_1 is Negative ! ")

# Else-if statement
Number_2 = 0 

if (Number_2 > 0):
    print(" Number_2 is Positive ! ")
elif (Number_2 < 0):  #In python else-if i written as elif
    print(" Number_2 is Negative ! ")
else:
    print(" Number_2 is Zero ! ")

# Example_2 : Classify Student percentage into distinction, 1st class, 2nd class etc ->

#Generic Synatax : <Return_Type>Function_name(input_parameters)

#python syntax : def Function_name(input_parameters)<Return_Type>

# ⬇️ Function Definition 
def GetClassForPercentage(percentage : float) -> str: # ⬅️ Function Declartion 
    if (percentage >= 75):
        return " Distinction "
    elif (percentage >= 60):
        return " First Class "
    elif (percentage >= 50):
        return " Second Class "
    elif (percentage >= 35):
        return " Third Class "
    else:
        return " Failed "

# Function Invocation ⬇️
Student_Percentage = 30
result = GetClassForPercentage (Student_Percentage)
print(result)

# Example_3 : Convert Day month in digit word ex : if input 5 then Return May

# switch Statement 
# Usaully Switch Statement does execute and jump to the statisfying case when it step into Function !
# But in python, its different as Python is ( Interpreted language ) the switch statement does not jump to satisfying case Immediately !
#It will go ( Line-by-Line ) Reading each case and excuting according to the declared condition ! 

#⬇️ Function Definition
def get_Month_str(Month : int) -> str: # ⬅️ Function Declartion 
    match (Month):
        case 1:
            return " January "
        case 2:
            return " February "
        case 3:
            return " March "
        case 4: 
            return " April "
        case 5:
            return " May "
        case 6:
            return " June "
        case 7:
            return " July "
        case 8: 
            return " August "
        case 9:
            return " September "
        case 10:
            return " October "
        case 11:
            return " November "
        case 12:
            return " December "
        case _:
            return " Invalid Input "

# Function Invocation ⬇️
print(get_Month_str ( - 1 ))
print(get_Month_str ( 1 ))
print(get_Month_str ( 5 ))
print(get_Month_str ( 10 ))
print(get_Month_str ( 15 ))

# Example_4 : Greater ( or ) Smaller number using conditional statements 

# Ternary_Operator 

Number_3 = 10

result = " Greater or Equal to Zero " if ( Number_3 >= 0 ) else " Less than Zero "

print(result)