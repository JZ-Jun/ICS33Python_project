#Description
#There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#Constraints
#The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
#The size of flights will be in range [0, n * (n - 1) / 2].
#The format of each flight will be (src, dst, price).
#The price of each flight will be in the range [1, 10000].
#k is in the range of [0, n - 1].
#There will not be any duplicated flights or self cycles.
#Methodology
#This is a graph question. We can solve it either by using BFS or Dijkstra.

def lowcost(n,edges,src,dst,k):
    dict1={} 

    
    for each in edges:
        if each[0] not in dict1:
            dict1[each[0]]=[each[1:]]    
        else:
            dict1[each[0]].append(each[1:])

    # dict1 = {0: [[1, 100], [2, 500]], 1: [[2, 100]]}
    
    list1=[]

    
    for each in dict1[src]:
        list1.append(each)

     # list1 = [[1, 100], [2, 500]]



    
    prise=-1 # If there is no such route, output -1.
    
    for i in range(k+1): #  find the cheapest price from src to dst with up to k stops
        
        for each in range(len(list1)):
            
            if list1[0][0]==dst: # If list1[0][0] is the destination.
                if prise==-1:
                    prise=list1[0][1] # If no other price has been recorded before, record this latest
                else:
                    prise=min(prise,list1[0][1]) # Compare the previously recorded prices, and then record the cheaper one.

            else: # If list1[0][0] is not the destination.
                if list1[0][0] in dict1:
                    
                    for each1 in dict1[list1[0][0]]:
                        
                        if each1[1]+prise>=prise and prise!=-1: # If this price is more expensive than the previously recorded price, ignore it.
                            

                            continue #  rejects all the remaining statements in the current iteration of the loop and moves back to the top of the loop. 
                            
                        
                        list1.append([each1[0],each1[1]+list1[0][1]]) 
                        
            list1.pop(0)

    return prise



# get input

n=int(input("n=")) # how many cities
edge=input("edges = ") # price between the 2 cities. for example:  [[0,1,100],[1,2,100],[0,2,500]]
edge=edge[2:-2].split("],[")
edges=[] 

for each in edge: # Put the user input in the correct format
    x=each.split(",")
    y=[]
    for each1 in x:
        y.append(int(each1))
    edges.append(y)
    
src=int(input("src = ")) # starting city
dst=int(input("dst = ")) # destination
k=int(input("k = ")) # up to k stops
print(lowcost(n,edges,src,dst,k))

## test cases:
##
##print(lowcost(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
##print(lowcost(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
##
##
