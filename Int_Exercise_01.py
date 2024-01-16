#Used to get a unique list of values from a given array
#Unique meaning they only occur once
def get_unique_list(a : list) -> list:

    unique = []
    match = 0

    for x in a:
    #To get the joke: https://en.wikipedia.org/wiki/Microsoft_XNA
        for y in a:
            if x == y:
                match+=1
    
        if match == 1:
            unique.append(x)  
        match = 0

    return unique

#
# Start of the Program
#
a_List = [1,22,22,35,8,9,8]

print("Original List:",end=' ')
print(a_List)
unique_list = get_unique_list(a_List)

print("Unique List:",end=' ')
print(unique_list, end='\n\n')
