#Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.

def findminmax(list1):
    if len(list1)==1:
        return (list1[0],list1[0])
    
    minx,maxx = findminmax(list1[1:])
    
    if list1[0]<minx:
        minx=list1[0]
        
    if list1[0]>maxx:
        maxx=list1[0]
        
    return (minx,maxx)


print(findminmax([-11,4,0,5,7,0,-1]))
