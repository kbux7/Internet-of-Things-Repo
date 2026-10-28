#Question6: Practice the four important operations: union (|), intersection (&), difference (-), and symmetric difference (^). 
#A = {1, 2, 3, 4}
#B = {3, 4, 5, 6}
#Find all unique elements in A and B. 
#Using the same sets, find elements common to both sets. 
#Find A - B and B - A. Explain why their results differ. 
#Find elements that are in either A or B, but not in both. 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. All unique elements in A and B (Union)
union_set = A | B
print("Union (All unique elements):", union_set)

# 2. Elements common to both sets (Intersection)
intersection_set = A & B
print("Intersection (Common elements):", intersection_set)

# 3. Difference (A - B and B - A)
diff_a_b = A - B
diff_b_a = B - A
print("A - B:", diff_a_b)
print("B - A:", diff_b_a)

# 4. Elements in either A or B, but not in both (Symmetric Difference)
sym_diff = A ^ B
print("Symmetric Difference:", sym_diff)