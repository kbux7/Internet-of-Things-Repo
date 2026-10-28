#Question3: data = {'a': 1, 'b': 2, 'c': 3}
#Create a dictionary where the original values become keys and keys become values.
#Output: {1: 'a', 2: 'b', 3: 'c'}

data = {'a': 1, 'b': 2, 'c': 3}

swapped_dict = {value: key for key, value in data.items()}

print(swapped_dict)