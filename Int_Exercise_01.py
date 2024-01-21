#Used to get a unique list of values from a given array
#Unique meaning they only occur once
def get_unique_list(a : list) -> list:

    unique = []
    match = 0

    #Moving through each element in the list
    for x in a:

        #Moving through the list again to check x against y
        for y in a:

            #if x equals y, we increment match
            if x == y:
                match+=1
    
        #if there is only one match, then the value is unique and add it to the list 
        if match == 1:
            unique.append(x)  

        #reset match
        match = 0

    return unique

#
# Start of the Program
#

#Test List
a_List = [1,22,22,35,8,9,8]

print("Original List:",end=' ')
print(a_List)
unique_list = get_unique_list(a_List)

print("Unique List:",end=' ')
print(unique_list, end='\n\n')
