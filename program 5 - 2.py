def countways(n,s):
    
    list1=findways(n,s) # the ways of making the change (a list of list) 
    # The order of coins does matter. So we are going to Delete duplicate content.

    
    list2=[]
    i=0
    
    for each in list1: # for each list in list1
        for each1 in list2:
            if sorted(each)==sorted(each1): # Check for any duplicate content
                i=1
            
        if i==0: # If this method is not duplicated, add it to list2. 
            list2.append(each)

        i=0 # set i back to 0
        
    print('solutions: {}'.format(list2)) # solutions
    return len(list2) # output


def findways(n,s,a=list()):
 
    # base case
    if n == 0:
        return a
    elif n < 0:
        return []
    
    i=[]
    
    for each in s:
        b = findways(n-each,s,a+[each]) #recursion

        if b == []:
            b=1

        elif type(b[0])==int:
            # b is a list. (the way of making the change)
            i.append(b)

        else:
            # b is a list of list (the ways of making the change)
            for each1 in b:
                i.append(each1)

    
    return i # the ways of making the change (a list of list) 
    # The order of coins does matter.

    
print(countways(4,{1,2,3}))
print(countways(10,{2,5,3,6}))
