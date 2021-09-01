'''
Using Dynamic Programming:  Giving user input which is string s , return the longest palindromic substring in s.
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

def ifpalstr(str1):
    x = len(str1)
    if x % 2 == 0:
        for i in range(x // 2):
            if str1[i] != str1[-i - 1]:
                return False
    else:
        for i in range(x // 2):
            if str1[i] != str1[-i - 1]:
                return False
    return str1


def longestpalstr(str1):
    x = len(str1)
    substr = ""
    i = 1
    if x == 1:
        return str1
    if ifpalstr(str1):
        return ifpalstr(str1)
    while i < x:
        a = longestpalstr(str1[0:i])
        b = longestpalstr(str1[i:])
        if len(a) > len(substr):
            substr = a
        if len(b) > len(substr):
            substr = b
        i += 1
    return substr


x = input("s = ")
i = 0
if len(x) > 1000:
    i = 1
    print("wrong input")
for each in x:
    if each not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
        print("wrong input")
        i = 1
        break
if i == 0:
    print(longestpalstr(x))
