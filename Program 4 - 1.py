# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

import re 

def removeLowercase():
    s = input('enter your string: ')

    ans = re.sub('[a-z]', '', s)

    return 'after removing lowercase substrings: '+ ans



print(removeLowercase())
