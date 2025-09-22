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