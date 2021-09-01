'''
Suppose we have an array of integers. We have to return the indices of two integers, such that if we add them up, 
we will reach to a specific target that is also given. Here we will take one assumption, that is always there will be one unique solution in the array, 
so no two set of indices for same target will be there.
Array is like A = [2, 8, 12, 15], and the target sum is 20. Then it will return indices 1 and 2, as A[1] + A[2] = 20.
Follow the pseudocode:
Define one map to hold the result called res
For index i in range 0 to n – 1 (where n is the number of elements in the array)
if target − A[i] is present in res
return res[target − A[i]] and i as indices
Otherwise put i into the res as res[A[i]]  = i
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

def GetTheIndices(A, target):
	res = {}
	for i in range(len(A)):
		if target - A[i] in res:
			return [res[target - A[i]], i]
		else:
			res[A[i]] = i


array = [2, 8, 12, 15]
SumToGet = 20
print(GetTheIndices(array, SumToGet))
