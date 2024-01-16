
def get_combined_dicts(dict1 : dict, dict2 : dict) -> dict:
    combo_dict : dict = {}
    for a,b in dict1.items():

        for c,d in dict2.items():
            if a == c:
                combo_dict[a] = b + d
                break

    return combo_dict

#
#   Program Start
#
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

combined_dict = get_combined_dicts(my_dict_1, my_dict_2)

print(combined_dict)
