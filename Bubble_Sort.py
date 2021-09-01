#1.Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 
#Write a Python program to sort a list of elements using the bubble sort algorithm. (With the user being able to give a list of integers as an input.

def bubbleSort(arr):
    # loop to access each array element.
    for i in range(len(arr)):
 
        # loop to compare array elements.
        for j in range(0, len(arr)-i-1):
            
            # to compare element and change their positions.
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 1, 4, 2, 8]

bubbleSort(arr)

# print the sorted array
print ("The sorted array is:")
print(arr)
