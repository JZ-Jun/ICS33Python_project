#Write a program that accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
def findnums(str1):
    list1 = str1.split()  # split string to a list of words
    list2 = []  # build an origin output list
    for each in list1:
        # check the word which have digit only
        i = 0
        for each1 in each:
            if each1 not in "1234567890":
                i = 1

        if i == 0:  # when all characters are digit i is still 0 then add it to the out put
            list2.append(each)
    print(list2)
    
