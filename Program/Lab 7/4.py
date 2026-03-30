class Student:
    def __init__(self):
        self.name = input("enter name: ")
        age_input = input("enter age: ")
        try:
            age = int(age_input)
            if age < 0:
                raise ValueError("age cannot be negative")
        except ValueError:
            print("error: invalid age age must be a non_negative integer")
            self.age = None
        else:
            self.age = age

    def display(self):
        print("Details:")
        print("Name:", self.name)
        print("Age:", self.age)
s = Student()
s.display()

input("________________________")
