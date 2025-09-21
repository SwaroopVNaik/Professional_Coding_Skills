# Example => 1 :
def Print_Star_Sequintial(MaxCount):
    star_string = ""
    for count in range(1, MaxCount, 1):
        star_string = star_string + "*" # Printing Squential Stars Using For Loops 

        print(star_string)

Print_Star_Sequintial(1000)

# Example => 2 :
def Print_Star_Squential_V2(MaxCount):
    print(MaxCount * "*")  # printing Squential Stars without using For loops

Print_Star_Squential_V2(1000)

def Print_Star_Grid(gridSize):

    for count in range(0, gridSize, 1):
        #"*" × gridSize = that many stars in one line.
        print(gridSize * "*") 

Print_Star_Grid(5)

# Example => 3 :
def print_star_from_list(numbers):

    for number in numbers:
        print(number * "*")

numbers = [2, 3, 4, 3, 2, 10, 11, 12 ,10, 12]
print_star_from_list(numbers)

# To Print Triangle : 
numbers = [1, 2, 3, 4, 5, 6]
print_star_from_list(numbers)
