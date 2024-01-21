
#This function takes in 2 dicts, and returns a dict that adds the integer values of shared string values
def get_combined_dicts(dict1 : dict[str, int], dict2 : dict[str,int]) -> dict:

    combo_dict : dict = {}
    
    #for every string and integer value in the first dict
    for a,b in dict1.items():
        
        #walk through the entire second dict
        for c,d in dict2.items():

            #if the string value of a is equal c , then we add then integer values b and d
            if a == c:
                #add a new map in the combo dict that shares the same string value and is mapped to the sum of the integers in the first 2 dicts
                combo_dict[a] = b + d
                break

    return combo_dict

#
#   Program Start
#
my_dict_1 : dict[str,int] = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 : dict[str,int] = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

combined_dict = get_combined_dicts(my_dict_1, my_dict_2)

print(combined_dict)
