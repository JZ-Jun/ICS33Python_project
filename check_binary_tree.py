'''
Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not.
Let a binary search tree (BST) is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

*A binary search tree (BST) is a node based binary tree data structure which has the following properties. 
• The left subtree of a node contains only nodes with keys less than the node’s key. 
• The right subtree of a node contains only nodes with keys greater than the node’s key. 
• Both the left and right subtrees must also be binary search trees.
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

class Tree:
    def __init__(self,head,left=None,right=None):
        self.head=head
        self.left=left
        self.right=right

def checkbest(tree,k=-1000):
    if tree!=None:
        if tree.head < k:
            return False
        if not checkbest(tree.left,k):
            return False
        k = tree.head
 
        return checkbest(tree.right,k)
    return True


tree1=Tree(6,Tree(4,Tree(3),Tree(5)),Tree(19,Tree(8)))
tree2=Tree(6,Tree(4,Tree(3),Tree(8)),Tree(19,Tree(5)))

print('check whether tree1 is a valid binary search tree (BST) or not:')
print(checkbest(tree1))
print('check whether tree2 is a valid binary search tree (BST) or not:')
print(checkbest(tree2))
