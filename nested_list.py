# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the names of any students(s) having the second lowest grade.
def findsecstu():
    num = int(input())
    totallist = []
    scorelist = []
    for k in range(0, num):
        name = input()
        score = float(input())
        totallist.append([name, score])
        if score not in scorelist:
            scorelist.append(score)
    scorelist = sorted(scorelist)
    secsc = scorelist[1]
    print()
    for each in totallist:
        if each[1] == secsc:
            print(each[0])


findsecstu()
