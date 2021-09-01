'''
Write a Python program to simulate an ecosystem containing two types of creatures, bears, and fish. 
The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. 
In each time step, based on a random process, each animal either attempt to move into an adjacent list location or stays where it is. 
If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, 
which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
'''
# Team member: Jun Zhu, Zhuoran Liu, Tongze Mao

import random


class River():  # the river class
    def __init__(self):

        self.riverList = ['N'] * 10  # the empty river

    def get_eco(self):
        self.numBear = 0
        self.numFish = 0

        for i in self.riverList:  # count the animals in river

            if i == 'B':
                self.numBear += 1

            elif i == 'F':
                self.numFish += 1
        print()

        print('Eco Status:', self.riverList)  # print river
        print('Number of Bears:', self.numBear)
        print('Number of Fish:', self.numFish)

    def move(self):
        # each animal either attempt to move into an adjacent list location or stays where it is. 
        time = 0
        stayOrMove = []
        leftOrRight = []
        while time < 10:  # for every element in list

            ifMove = random.randint(0, 1)  # 0 means stay, 1 means move
            stayOrMove.append(ifMove)

            direction = random.randint(3, 4)  # 3 means left, 4 means right
            leftOrRight.append(direction)
            time += 1

        for n in range(10):
            if self.riverList[n] == 'N':  # only animals will move
                stayOrMove[n] = 0

        for n in range(10):

            if self.riverList[n] != 'N':  # only animals will move

                if stayOrMove[n] == 1:  # the animal move

                    # n is position (index).

                    if n == 0:  # n = 0 means the animal is at the left most position. it can only move to right

                        if self.riverList[n + 1] == 'N':  # if the right side position is empty

                            self.riverList[n + 1] = self.riverList[n]
                            self.riverList[n] = 'N'  # the animal move to right
                            print('the animal at', n, 'moves to right')

                        elif self.riverList[n + 1] == 'F':  # if the right side position is fish

                            if self.riverList[n] == 'B':  # if the animal is a bear
                                self.riverList[n + 1] = self.riverList[n]
                                self.riverList[n] = 'N'  # the bear eats the fish and moves to right
                                print('the bear at', n, 'eats the fish and moves to right')

                            elif self.riverList[n] == 'F':  # if the animal is a fish
                                flag = 'false'

                                print('the fish at 0 moves to right')

                                for i in self.riverList:
                                    if i == 'N':
                                        flag = 'true'  # there is at least one empty position in list

                                if flag == 'false':
                                    print('the river is full, no empty space for the new baby!')

                                orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                random.shuffle(orderList)

                                if flag == 'true':
                                    '''
                        If two animals of the same type are about to collide in the same cell,
                        then they stay where they are, but they create a new instance of that type of animal,
                        which is placed in a random empty (i.e., previously None) location in the list.

                                    '''
                                    for i in orderList:
                                        if self.riverList[i] == 'N':  # if the position is empty
                                            self.riverList[i] = 'F'  # add the new born fish into the list
                                            print('2 bear meets, a new bear born at', i)

                                            break

                        else:  # if the right side is a bear

                            if self.riverList[n] == 'F':  # if the animal is a fish. the fish move to right

                                self.riverList[n] = 'N'  # the fish was killed by bear
                                print('the fish at', n, 'moves to right and was killed by bear')

                            elif self.riverList[n] == 'B':  # if the animal is a bear, two bear meets, a new bear born
                                flag = 'false'
                                print('the bear at 0 moves to right')

                                for i in self.riverList:
                                    if i == 'N':
                                        flag = 'true'  # there is at least one empty position in list

                                if flag == 'false':
                                    print('the river is full, no empty space for the new baby!')

                                orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                random.shuffle(orderList)

                                if flag == 'true':
                                    for i in orderList:
                                        if self.riverList[i] == 'N':  # if the position is empty
                                            self.riverList[i] = 'B'  # add the new born bear into the list
                                            print('2 bear meets, a new bear born at', i)

                                            break
                    elif n == 9:  # n = 9 means the animal is at the right most position. it can only move to left

                        if self.riverList[n - 1] == 'N':  # if the left position is empty

                            self.riverList[n - 1] = self.riverList[n]
                            self.riverList[n] = 'N'  # the animal moved to left
                            print('the animal at', n, 'moves to left')

                        elif self.riverList[n - 1] == 'F':  # if the left position is a fish

                            if self.riverList[n] == 'B':  # if the animal is a bear
                                self.riverList[n - 1] = self.riverList[n]  # the bear kills the fish
                                print('the bear at', n, 'kills the fish and moves to left')
                                '''
                                 If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
                                 '''
                                self.riverList[n] = 'N'  # the bear move to left

                            elif self.riverList[n] == 'F':
                                flag = 'false'
                                print('the fish at 9 moves to left')

                                for i in self.riverList:
                                    if i == 'N':
                                        flag = 'true'  # there is at least one empty position in list

                                if flag == 'false':
                                    print('the river is full, no empty space for the new baby!')

                                orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                random.shuffle(orderList)

                                if flag == 'true':
                                    for i in orderList:
                                        if self.riverList[i] == 'N':  # if the position is empty
                                            self.riverList[i] = 'F'  # add the new born fish into the list
                                            print('2 fish met, and a new fish was born at', i)

                                            break

                        else:  # if the left is a bear

                            if self.riverList[
                                n] == 'F':  # the animal is a fish, the fish moved to left and met the bear

                                self.riverList[n] = 'N'  # the fish was killed by bear
                                print('the fish at', n, 'moves to left and was killed by the bear')

                            elif self.riverList[n] == 'B':  # if the animal is a bear, two bear meets, a new bear born
                                flag = 'false'
                                print('the bear at 9 moves to left')

                                for i in self.riverList:
                                    if i == 'N':
                                        flag = 'true'  # there is at least one empty position in list

                                if flag == 'false':
                                    print('the river is full, no empty space for the new baby!')

                                orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                random.shuffle(orderList)

                                if flag == 'true':
                                    for i in orderList:
                                        if self.riverList[i] == 'N':  # if the position is empty
                                            self.riverList[i] = 'B'  # add the new born bear into the list
                                            print('2 bears met and a new bear was born at', i)

                                            break

                    else:  # if the animal is neither at the first nor the last of the list

                        if leftOrRight[n] == 3:  # if the direction is to left

                            if self.riverList[n - 1] == 'N':

                                self.riverList[n - 1] = self.riverList[n]
                                print('the animal at', n, 'moves to left')
                                self.riverList[n] = 'N'

                            elif self.riverList[n - 1] == 'F':

                                if self.riverList[n] == 'B':
                                    self.riverList[n - 1] = self.riverList[n]
                                    print('the bear at', n, 'moves to left and eats the fish')
                                    self.riverList[n] = 'N'

                                elif self.riverList[n] == 'F':
                                    flag = 'false'
                                    print('the fish at', n, 'moves to left')

                                    for i in self.riverList:
                                        if i == 'N':
                                            flag = 'true'  # there is at least one empty position in list

                                    if flag == 'false':
                                        print('the river is full, no empty space for the new baby!')

                                    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    random.shuffle(orderList)

                                    if flag == 'true':
                                        for i in orderList:
                                            if self.riverList[i] == 'N':  # if the position is empty
                                                self.riverList[i] = 'F'  # add the new born fish into the list
                                                print('2 fish met and a new fish was born at', i)

                                                break

                            else:  # if the left is a bear

                                if self.riverList[n] == 'F':

                                    self.riverList[n] = 'N'  # the fish was killed by bear
                                    print('the fish at', n, 'moves to left and was killed by the bear')

                                elif self.riverList[n] == 'B':
                                    flag = 'false'
                                    print('the bear at', n, 'moves to left')

                                    for i in self.riverList:
                                        if i == 'N':
                                            flag = 'true'  # there is at least one empty position in list

                                    if flag == 'false':
                                        print('the river is full, no empty space for the new baby!')

                                    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    random.shuffle(orderList)

                                    if flag == 'true':
                                        for i in orderList:
                                            if self.riverList[i] == 'N':  # if the position is empty
                                                self.riverList[i] = 'B'  # add the new born bear into the list
                                                print('2 bear met and a new bear was born at', i)

                                                break
                        else:  # if the direction is to right

                            if self.riverList[n + 1] == 'N':

                                self.riverList[n + 1] = self.riverList[n]
                                print('the animal at', n, 'moves to right')
                                self.riverList[n] = 'N'

                            elif self.riverList[n + 1] == 'F':

                                if self.riverList[n] == 'B':
                                    self.riverList[n + 1] = self.riverList[n]
                                    print('the bear at', n, 'moves to right and eats the fish')
                                    self.riverList[n] = 'N'

                                elif self.riverList[n] == 'F':
                                    flag = 'false'
                                    print('the fish at', n, 'moves to right')

                                    for i in self.riverList:
                                        if i == 'N':
                                            flag = 'true'  # there is at least one empty position in list

                                    if flag == 'false':
                                        print('the river is full, no empty space for the new baby!')

                                    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    random.shuffle(orderList)

                                    if flag == 'true':
                                        for i in orderList:
                                            if self.riverList[i] == 'N':  # if the position is empty
                                                self.riverList[i] = 'F'  # add the new born fish into the list
                                                print('2 fish met and a new fish was born at', i)

                                                break
                            else:  # if the right is a bear

                                if self.riverList[n] == 'F':

                                    self.riverList[n] = 'N'  # the fish was killed by bear
                                    print('the fish at', n, 'moves to right and was killed by the bear')

                                elif self.riverList[n] == 'B':
                                    flag = 'false'
                                    print('the bear at', n, 'moves to right')

                                    for i in self.riverList:
                                        if i == 'N':
                                            flag = 'true'  # there is at least one empty position in list

                                    if flag == 'false':
                                        print('the river is full, no empty space for the new baby!')

                                    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    random.shuffle(orderList)

                                    if flag == 'true':
                                        for i in orderList:
                                            if self.riverList[i] == 'N':  # if the position is empty
                                                self.riverList[i] = 'B'  # add the new born bear into the list
                                                print('2 bear met and a new bear was born at', i)
                                                break

        return self.riverList

    def add_bear(self, n):
        print()
        print('you want to add bear to', n)
        if self.riverList[n] == "B":
            print("Rejected: Already occupied by a bear.")

            print()

        elif self.riverList[n] == "N":
            self.riverList[n] = "B"
            print()
            print('you added a bear at', n)
            print()

        else:
            print("Bear eats Fish!")
            self.riverList[n] = "B"
            print()

        print('after the randomly move:')
        print(self.move())

    def add_fish(self, n):
        print()
        print('you want to add fish to', n)

        if self.riverList[n] == "F":
            print("Rejected: Already occupied by a fish.")
            print()

        elif self.riverList[n] == "N":
            self.riverList[n] = "F"
            print()
            print('you added a fish at', n)
            print()
        else:
            print("Rejected: Already occupied by a bear.")
            print()

        print('after the randomly move:')
        print(self.move())

    def kill(self, n):
        print()

        print('you killed the animal at', n)
        self.riverList[n] = "N"

        print()


data = River()
print("Adding a fish or a bear")
print()

print('Warning: when you use the add function, based on a random process, \
each animal either attempt to move into an adjacent list location or stays where it is.')
print()

data.add_bear(3)
data.add_bear(4)

data.add_fish(7)
data.add_fish(1)

data.add_bear(2)
data.add_fish(8)

data.get_eco()

data.kill(2)
data.get_eco()

data.kill(7)
data.get_eco()

print()
print('end')
