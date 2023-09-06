# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]



number = [1,2,3,4,5,6,7]

def triple(x):
   return 3*x 

triple_num = map(triple, number)
print(list(triple_num))








