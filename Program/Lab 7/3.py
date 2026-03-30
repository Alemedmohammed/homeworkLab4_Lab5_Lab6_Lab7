class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def add_bonus(self, bonus):
        self.salary += bonus

    def display(self):
        print(f"name: {self.name}, total salary: {self.salary}")
m = Manager("maryam", 5000)
m.add_bonus(1000)
m.display()
input("________________________")