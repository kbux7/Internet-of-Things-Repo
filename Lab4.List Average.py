#Question2: Write a Python program to find the average of all the numbers in the following list:
#my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
#Use a for loop to calculate the sum of the numbers and then find and print their average.

mylist = [3,1,0,9,5,2,6,4,9,8,7]
total_no =0
for i in mylist:
    total_no += i
print(f'Average: {total_no/11}')