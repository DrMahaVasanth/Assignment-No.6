class dog:

    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        print("Details of the dog:")
        print("\nName: ", self.name, "\nAge (in months): ",self.age)

    def get_info(self):
        print("Color: ", self.coat_color)

class JackRussellTerrier(dog):

    def description(self):
        super().__init__(self.name,self.age,self.coat_color)
        print("\nDetails of the dog:")
        print("\nName: ", self.name, "\nAge (in months): ",self.age)

    def get_info(self):
        super().__init__(self.name,self.age,self.coat_color)
        print("Color: ", self.coat_color)

class Bulldog(dog):

    def description(self):
        super().__init__(self.name,self.age,self.coat_color)
        print("\nDetails of the dog:")
        print("\nName: ", self.name, "\nAge (in months): ",self.age)

    def get_info(self):
        super().__init__(self.name,self.age,self.coat_color)
        print("Color: ", self.coat_color)

obj_dog=dog("Blackberry",6,"Black")
obj_jrt=JackRussellTerrier("Jack Russell Terrier",10,"White & Tan")
obj_bd=Bulldog("Bull Dog",12,"white")

obj_dog.description()
obj_dog.get_info()

obj_jrt.description()
obj_jrt.get_info()

obj_bd.description()
obj_bd.get_info()
