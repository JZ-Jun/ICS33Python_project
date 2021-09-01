'''
Find intersecting nodes of a linked list.
Given the user input of two singly linked lists that intersect at some point, find the intersecting node. 
Create two linked lists
1st Linked list is 3.6.9.15.30
2nd Linked list is 10.15.30
15,30 is the intersection point
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next  

LL=Node(3)
LL.next=Node(6)
LL.next.next=Node(9)
LL.next.next.next=Node(15)
LL.next.next.next.next=Node(30)
L=Node(10)
L.next=Node(15)
L.next.next=Node(30)


def fun1(LL,L):
    list1=[]
    list2=[]
    list3=[]
    while True:
        list1.append(LL)
        LL=LL.next
        if LL==None:
            break
    while True:
        list2.append(L)
        L=L.next
        if L==None:
            break
    len_of_list1 = len(list1)
    len_of_list2 = len(list2)
    for each in list1:
        for each1 in list2:
            if each.data==each1.data:
                list3.append(each)
    return [len_of_list1, len_of_list2, list3]


fun_res = fun1(LL,L)
for each in fun_res[2]:
    print(each.data, end=" ")
print("is the intersection point.")

print(f"length of list1: {fun_res[0]}")
print(f"length of list2: {fun_res[1]}")
