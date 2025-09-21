# For Loops 
# Remember: If we know the number of items , then we must use ( for ) loop 
# Range( Start(0), Stop(11), Step(1) -> (Increment)
# Stop 11 takes less then 11

for Index in range (1, 11, 1):
    print(Index)

# List
names = [ " swaroop ", " svn ", "naik" ]

# Even to iterate Items ( for ) loop will be used
for name in names:
    print( name )
    print(name.upper())

# While Loop 
count = 0 # Start 
while(count <= 10): # Stop 
    print(count)
    count = count + 1 # Step

# range(stop)
# stop -> 10
# method_1: In this method_1 range function it takes only 1 argument with the maximum value ( 10 ) ! 

values = range(10)

for item_1 in values:
    print( item_1 )

# Range(start, stop, step)
# start -> 0, stop -> 10, step -> 1
# method_2: In this method_2 range Function it takes 3 arguments (start -> 0, stop -> 10 , step -> 1) with max value ( 10 ) !
# In c for(int index = 0; index <= 10; index ++)
for item_2 in range(0, 10, 1):
    print( item_2 )

# Range(start, stop, step)
# start -> 1, stop -> 10, step -> 2
# In c (int index = 1; index <= 10; index += 2)

for item_3 in range(1, 10, 2): 
    print( item_3 )

# Range(start, stop, step)
# start -> 10, stop -> 1, step -> -1 (Reverse 10 -> 9)
# for (int index = 10; index > 1; index --) ( In c )

for item_4 in range(10, 1, -1):
    print(item_4)

# for loop multiplication ( Nested - for loop )
for i in range(2, 11):
    print(f"Multiplication table for {i}")
    #Loop through number 1 to 10 to multiply with 'i'
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# breaking out  for loop 
for number in range(10):
    if number == 5:
        print( " Breaking the Loop at  5 " )
        break;
    print(number) 

# Continue in for loop 

names = [ " swaroop ", " svn ", "naik" ]

for name in names:
    if(name == " swaroop "):
        continue
    print(name)

# Good Example :

squares = [number ** 2 for number in range(6)]
print(squares)

#Summary 

# 1 -> Use ( for ) to iterate over any iterable objects 
# 2 -> use ( range() ) for numeric iterations
# 3 -> enumerate() is useful when you neeed indexes
# 4 -> for else () is unique python feature 
numbers = [24, 7, 5, 1]

for number in numbers:
    print(number)
    if(number == 5 ):
        print(" 3 is found so breaking ")
    else:
        print(" 3 is not found ")

# 5 -> break and continue after loop behaviour 
# 6 -> List comprehesnsions are a concise way to create lists 