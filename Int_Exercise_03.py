
def string_to_Dict(string : str) -> dict:
    given = string.lower()
    given = given.split(" ")
    fullStr = ""
    for a in given:
        fullStr += a
    count : int = 0
    outputDict : dict = {};
    for a in fullStr:
        for b in fullStr:
            if a == b:
                count += 1
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
        if s_input.isspace():
            raise ValueError
        break 
    except ValueError:
        print("That value is incorrect,", end=' ')


final = string_to_Dict(s_input)
print(final, end='\n\n')
