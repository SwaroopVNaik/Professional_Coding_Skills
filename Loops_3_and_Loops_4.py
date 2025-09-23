# Example 1 ->
# The function `print_star_grid_concatenation` takes a single number as input.
def print_star_grid_concatination(gridSize):
    # This loop runs for each row we need to print.
    for row in range(gridSize):
        # We start with an empty list to build our row.
        printMsg = []
        # This loop adds a star to our list for each column.
        for noofstars in range(gridSize):
            printMsg.append("*")
        # We combine all the stars in the list into a single string and print it.
        print("".join(printMsg))

# This will print a 5x5 grid of stars.
print_star_grid_concatination(5) 

# Example 2 :-> Print_Star only at edges 

def Print_Star_only_at_Edges(GridSize):
    for row in range(1, GridSize + 1, 1):
        printMsg = []

        for column in range(1, GridSize + 1, 1):
            isStar = column == 1 or column == GridSize or row == 1 or row == GridSize

            printMsg.append("* " if isStar else "  ")
            
            # printMsg.append(str(row)  + " , " + str(column) + " ")

        print(" ".join(printMsg))

Print_Star_only_at_Edges(5)

# Example 3 :-> Calculate and create string with spaces (Pyramid Pattern) ! 
# Calculate and create stars
# print stars + new Line

def print_star_pyramid(height):

    noOfStars = 1
    for level in range (1, height, 1):
        noofspaces = height - level
        print(noofspaces * " " + noOfStars * "*")
        noOfStars = noOfStars + 2 

print_star_pyramid(15)

# Example 4 :-> Inverted Pyramid ! 
def print_inverted_star_pyramid(height):

    for level in range(1, height + 1, 1):

        noOfSpaces = level - 1 
        noOfstars = (height - level ) * 2 + 1
        print(noOfSpaces * " " +  noOfstars * "*")

print_inverted_star_pyramid(15)