#Write a recursive program to find the first uppercase letter in a string (Iterative and Recursive)

s = "absQDog"


def findfirstupper(s):
    if len(s) == 0:
        return "None"
    if s[0].isupper():
        return s[0]
    return findfirstupper(s[1:])


print(findfirstupper(s))
