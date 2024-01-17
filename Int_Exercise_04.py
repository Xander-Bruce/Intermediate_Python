
print()
count : int = 0
sum : int = 0
while count <=4:
    try:
        sum += int(input("Enter Integer #" + str(count+1) + ": "))
        count += 1

    except ValueError:
        print("Invalid Input, please enter an int")

print("\nYour sum is: " + str(sum), end='\n\n')
