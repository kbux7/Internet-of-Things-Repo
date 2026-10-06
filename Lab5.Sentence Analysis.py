#Question2: Ask the user to enter a sentence.
#Display:
# Number of characters
# Number of words
# Number of vowels
# Number of spaces
# Number of digits

vowels = 0
spaces = 0
digits = 0

sentence = str(input('Enter a sentence: '))
vowel_list = "aeiouAEIOU"

for char in sentence:
    if char in vowel_list:
        vowels += 1

for char in sentence:
    if char == " ":
        spaces += 1
        
    if char.isdigit():
        digits += 1
    

print(f'\nNumber of characters: {len(sentence)}')
print(f'Number of words: {len(sentence.split(" "))}')
print(f'Number of vowels: {vowels}')
print(f'Number of spaces: {spaces}')
print(f'Number of digits: {digits}')