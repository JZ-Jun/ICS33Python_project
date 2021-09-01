'''
Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse. For example, racecar and
gohangasalamiimalasagnahog are palindromes. (FYI strings are alphanumeric).(No loops)
'''
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
