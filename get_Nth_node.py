#Write a function to get Nth node in a Linked List

class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next  
class LinkedList:

    def __init__(self):
        self.head = None
        self.head1=None


    def getNode(self, n):
        node = self.head1
        
        for each in range(1,n+1):
            if n==each:
                print('when n =',n,'the node is:', node.data)
                return
            else:
                node=node.next
        
        print('n =',n,'is not in range')
        return


    def addNode(self, data):
        if self.head==None:
            self.head1 = Node(data)
            self.head = self.head1
        else:
            self.head.next=Node(data)
            self.head=self.head.next


LL = LinkedList()
LL.addNode(0)
LL.addNode(13)
LL.addNode(5)
LL.addNode(46)
LL.addNode(7)
LL.addNode(30)
n = int(input('Which node do you want to get: n = '))
LL.getNode(n)
