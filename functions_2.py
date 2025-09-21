#Function Definition 
def Do_Nothing() -> None:  #ReturnType (Optional) In python
    pass 

#if we have not given any instructions in python inside a function we must declare pass 

#function Definition 
def Print_message() ->  None:
    #Indentation is very-very important in python  (Important !)
    # Its like curly braces in Python 
    #always the indentation should have a tab (key) space
    #usually if we leave 1 space for indentation the python program will run but as industry practice we must leave tab (key) Space.
    #tab == 4 blank - space
    print("Namaskara Bharath !")

#this above 👆 function will not print anything unless, the function is Inovoked/Called 

#function Invocation/Calling the function 

#The function which python Interpreter will execute must always start from the pos->1 without any indentation space (Important !)
#if we give indentation space to function invocation the program will run but the function output will not be printed (Important !)
 
Do_Nothing()
Print_message()

#after calling the function the print_message will be printied

#2) Calling One Function with another Function (Self - loop) (Important !)

#Function Defintion
def First_Function() -> None:
    print("I Am First Function")
    Second_Function()

def Second_Function() -> None:
    print("I am Second Function")
    First_Function()

#function Invocation/Calling Function
First_Function()
Second_Function()

# In Python, function must be defined before calling/invocation
# Because Python is interpreted -> executes line by line
# If you call before defining -> ERROR

# In C, function can be called before definition
# If no prototype -> WARNING
# If prototype is given -> NO issue
# Because C is compiled -> compiler checks whole code first

#note -> Recurrsion Means Same function Calling itself (Important !)

#3) Function with Parameters 

#first Method ->
def print_student_details(name : str, Age : int, CGPA : float) -> int:
    print("Student Name is :", name)
    print("Student age is :", Age)
    print("Student CGPA is :", CGPA)
    return Age, name

Student_age, Student_name = print_student_details("Swaroop", 21, 7.3)
print("student age returned is = ", Student_age)
print("Student name returned is =", Student_name)

#second method ->
def print_student_details(name , age, cgpa):
    print("Student Name is :", name)
    print("Student age is :", age)
    print("Student CGPA is :", cgpa)

print_student_details("SVN", 21, 7.3)

#how to write function name and decide its input and output (Very-Very Important !)

#example Task : 
#who is the topper
#which subject => maths 
#which grade => 5th grade
#which School => JNV
#name of student ?
#deciding input :subject, grade, school
#deciding output :Student Name 

def get_topper_name(subject :str, grade : int, school_name :str, student_name : str) -> str:
    #Dummy Implementation
    return student_name

student_name = get_topper_name("Maths", 5, "Novodya", "Ram")
print("topper Student name = ", student_name)

def get_school_name(SchoolID :int) -> str:
    return "Navodya"

def get_boys_girls_count_for_grade_in_school(schoolId : int, grade : int)-> tuple[int,int]:
#actual code to connect to DB, file or Api goes here
    return 100, 100;

boys_count, girls_count = get_boys_girls_count_for_grade_in_school(1, 5)
print("Count of boys and Girls =", girls_count, boys_count)