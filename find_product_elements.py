'''
Get the product of all other elements
Given an array of integers, return a new array such that each element at index I of the new array is the product of all the numbers in the original array except the one at i.
For example:
if our input is [1,2,3,4,5], the expected output would be [120, 60,40,30,24]
if our input [3,2,1] the expected output be [2,3,6]
'''

def turnli(x):
    outlist = []
    length = len(x)
    for num in range(0, length):
        k = 1
        list1 = x.copy()
        del list1[num]
        for each in list1:
            k = k * each
        outlist.append(k)
    return outlist


print(turnli([1, 2, 3, 4, 5]))
print(turnli([3, 2, 1]))
