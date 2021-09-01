#Explain Inheritance in Python with an example.
class Staff:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def printname(self):
        print(self.first_name, self.last_name)


x = Staff("Isaac", "Alice")
x.printname()


class Teacher(Staff):
    pass


y = Teacher('Tom', 'Bob')

y.printname()
