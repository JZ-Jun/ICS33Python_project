# A palindrome is a word, number, phrase, or other sequences of characters which reads the same backward as forward, such as racecar, mom, or 121.
# Given a list, count and print all the palindrome numbers in it.
# Example:
# Input: 10 121 133 155 141 252 Output: 121 141 252 Total palindrome nos. are 3

def countpalnum(list1):
    i = 0
    listout = []
    for each in list1:
        num = str(each)
        length = len(num)
        k = 0
        for each1 in range(0, length):
            if num[each1] != num[-each1 - 1]:
                k = 1
        if k == 0:
            i += 1
            listout.append(int(num))
    for each in listout:
        print(each, end=" ")
    print("Total palindrome nos. are " + str(i))


x = input()
x = x.split()
countpalnum([10, 121, 133, 155, 141, 252])
