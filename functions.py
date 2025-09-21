# 1) Functions with No Parameters, No Return

#Function Definition
def say_hello():  # -> Function Declaration (without colon)
    print("hello ! Welcome to functions")

#Function Invocation / Calling 
say_hello()

# 2) Functions with Paramenters(Input Arguments) , No Return 

#Function Definition
def greet(name): # -> Function Declaration (without colon)
    print(f"Hello {name}, Good to see you")

#Function Invocation / Calling
greet("swaroop")

# 3) Functions with paramenters and Return Value

#Function Definition
def add_numbers(a, b): # -> Function Declaration (without colon)
    return a + b

#Function Invocation 
Sum = add_numbers(10 , 20)
print(Sum) 

# 4) Function with default parameter 

#Function Definition 
def greet_user(name = "Guest"): # -> Function Declaration (without colon)
    print(f"Hello {name}, Welcome")

#Function Innvocation / Calling
greet_user("Swaroop") #Custom
greet_user() #Default

# 5) Function Returning Function Value

#Function Definition 
def get_details():  # -> Function Declaration (without colon)
    Student_name = "Swaroop"
    Student_age = 21
    Student_course = "Python"
    return Student_name, Student_age, Student_course

#Function Innvocation / Calling
name, age, course = get_details()
print("Name: ", name)
print("Age :", age)
print("Course :", course)

# 6) Square of Number

#Function Definition
def Square_Number(number): # -> Function Declaration (without colon)
    return (number * number)

#Function Invocation / Calling
Answer = Square_Number(5)
print(Answer)

# 7) Convert Celsius To Faherenheit (Formula: F = ( C * 9/5 ) + 32)

#Function Definition 
def Celsisus_to_Faherenheit(Celsisus): # -> Function Declaration(without colon)
    return (Celsisus * 9/5 )+ 32

#Function Invocation / Calling 
Converted_Temperature = Celsisus_to_Faherenheit(100) 
print(Converted_Temperature)

#------------------------Functions Part - 2 ---------------------------

#warm-up 1 
message = "Namaskara Bharath...!"
print(message)

#warm-up 2
maths = 90
science = 80
Kannada = 95
English = 85
Social_Science = 90

total = maths + science + Kannada + English + Social_Science

print("Total Marks for the student ", total)

