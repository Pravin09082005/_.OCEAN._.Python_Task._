def dict_Swap(dictionary):
    return {value: key for key, value in dictionary.items()}

A = {'a': 1, 'b': 2, 'c': 3}
swapped_dict =dict_Swap(A)
print("Original dictionary:", A)
print("Swapped dictionary:", swapped_dict)
