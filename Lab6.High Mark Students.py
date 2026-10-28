#Question2: marks = {
#    'Ali': 85,
#    'Sara': 95,
#    'Ahmed': 95,
#    'Noor': 78
#     }
#Print every student who achieved the highest marks and their marks.
#Expected toppers: Sara and Ahmed.

marks = {'Ali': 85, 'Sara': 95, 'Ahmed': 95, 'Noor': 78}

highest_marks = max(marks.values())

print("Expected toppers:")
for name, score in marks.items():
  if score == highest_marks:
    print(f"{name} with {score} marks")