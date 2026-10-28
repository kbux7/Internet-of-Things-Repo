#Question1: Count how many times each number occurs and store the result in a dictionary.
#Input: [2, 3, 2, 5, 3, 2, 5, 8]
#Output: {2: 3, 3: 2, 5: 2, 8: 1}
#Do not use count().

nums = [2, 3, 2, 5, 3, 2, 5, 8]
frequency_dict = {}

for num in nums:
  frequency_dict[num] = frequency_dict.get(num, 0) + 1

print(frequency_dict)