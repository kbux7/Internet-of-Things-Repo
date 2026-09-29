#Question4: Create an empty list: 
#shopping = [] 
#Ask the user to enter 5 shopping items. 
#Then display the complete shopping list.
 
shopping = []
for i in range(5):
    item = str(input(f"Enter {i+1} shopping item: "))
    shopping.append(item)
print("Complete shopping list:")
for item in shopping:
    print(item)