#Question4: Input:
#words = ['apple', 'ant', 'banana', 'ball', 'cat']
#Expected output: 
#{
#    'a': ['apple', 'ant'],
#    'b': ['banana', 'ball'],
#    'c': ['cat']
#}
#Build the dictionary using loops and conditions. 

words = ['apple', 'ant', 'banana', 'ball', 'cat']
grouped_dict = {}

for word in words:
  first_letter = word[0]
  if first_letter not in grouped_dict:
    grouped_dict[first_letter] = []
  grouped_dict[first_letter].append(word)

print(grouped_dict)