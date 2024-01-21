
#Takes in a string and returns a dict mapping each character in the string to an integer value with how many times it occurs in the string
def string_to_Dict(string : str) -> dict[str, int]:

    #changes all letters to lower case
    given = string.lower()
    #splits the string on spaces
    given = given.split(" ")
    fullStr : str = ""

    #add all of the split strings together
    for a in given:
        fullStr += a

    count : int = 0

    outputDict : dict[str, int] = {};

    #for every character in the fullstr
    for a in fullStr:

        #walk through the fullstr again
        for b in fullStr:

            #if a character is equal to another character in the string, then we increment the count of that character
            if a == b:
                count += 1

        #map the character to the number of times that character occurs in the string.
        outputDict[a] = count
        count = 0

    return outputDict;


#
# Program Start
#
print()
while True:
    try:
        
        s_input : str = input("Please enter a word, quote or phrase: ")

        #if the user input is just a space, throw an error
        if s_input.isspace():
            raise ValueError

        #if the user input is just a number throw an error
        if s_input.isnumeric():
            raise ValueError

        break 
    except ValueError:
        print("That value is incorrect,", end=' ')


final = string_to_Dict(s_input)
print(final, end='\n\n')
