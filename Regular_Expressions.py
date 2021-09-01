'''
Using Regular Expressions
Write a Python program to remove lowercase substrings from a given string. (A user should be able to give input). 
Original string: KDeoALOklOOHserfLoAJSIskdsf After removing lowercase letters, above string becomes: KDALOOOHLAJSI
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

import re 

def removeLowercase():
    s = input('enter your string: ')

    ans = re.sub('[a-z]', '', s)

    return 'after removing lowercase substrings: '+ ans



print(removeLowercase())
