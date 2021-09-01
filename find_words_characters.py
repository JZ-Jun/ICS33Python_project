#Write a Python program to find all words which are at least 4 characters long in a string. 

def find4words(str1):
    list1 = str1.split()  # return the string to a list of words
    list2 = []  # build an origin list for output
    for each in list1:
        if len(each) >= 4:  # choose the word at least 4 characters
            list2.append(each)  # add the word to output list
    return list2
