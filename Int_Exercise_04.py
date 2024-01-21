
print()
count : int = 0
sum : int = 0

#Take in input from the user and if it is not an integer throw an error
while count <=4:
    try:
        sum += int(input("Enter Integer #" + str(count+1) + ": "))
        count += 1

    except ValueError:
        print("Invalid Input, please enter an int")

#Print the sum of the given integers
print("\nYour sum is: " + str(sum), end='\n\n')
