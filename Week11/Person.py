class Person():
    def __init__(self, p_name, p_age, p_height):
        self.name = p_name
        self.age = p_age
        self.height = p_height
        self.public_prop = "I am public property"

        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, new_name):
            self._name = new_name

        def __del__(self):
            print("The garbage collector is automatically destroying person objects")


person1 = Person("John", 25, 5.8)
print("The name of the person is: ", person1.name)
person1.name = "Alfred"
print("The name of the person is: ", person1.name)