'''
Write a Python program to simulate an ecosystem containing two types of creatures, bears, and fish. 
The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. 
In each time step, based on a random process, each animal either attempt to move into an adjacent list location or stays where it is. 
If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, 
which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao


def ifpad(s):
    
    if len(s)==0 or len(s)==1:
        print('the string s is a palindrome')
        return True
    
    
    elif s[0]==s[-1]:
        return ifpad(s[1:-1])
    
    else:
        print('the string s is not a palindrome')
        return False


ifpad('civic')
ifpad('noon')
ifpad('mom')
ifpad('food')
