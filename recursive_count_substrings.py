#Give the recursive solution to count substrings with the same first and last characters.
def findsub(s):
    if (len(s) == 1):
        return 1
    if (len(s) <= 0):
        return 0
    result = findsub(s[1:]) + findsub(s[0:-1]) - findsub(s[1:-1])
    if s[0] == s[-1]:
        result += 1
    return result
