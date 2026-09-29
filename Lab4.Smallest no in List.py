#Question1: Write a Python program to find the smallest number in the following list using a for loop. 
#my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
#Print the smallest number as the output.

mylist = [3,1,0,9,5,2,6,4,9,8,7]
smallest_no = mylist[0]
for i in mylist:
    if i < smallest_no:
        smallest_no = i
print(f'Smallest number: {smallest_no}')