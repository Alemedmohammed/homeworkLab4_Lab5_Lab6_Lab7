class person:
    def __init__(self, name, age):
        self.name = name       
        self.__age = age       
    def set_age(self, new_age):
        self.__age = new_age
    def get_details(self):
        return f"name: {self.name}, age: {self.__age}"
p = person("maryam", 30) 
p.set_age(25)
print(p.get_details())
input("________________________")