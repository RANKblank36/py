class Dog:

    animal = "Dog"

    def __init__(self, breed, colour):

        self.breed = breed
        self.colour = colour

    def show_details(self):
        print(f"Animal : {Dog.animal}")
        print(f"Breed  : {self.breed}")
        print(f"Colour : {self.colour}")
        print("-" * 25)

dog1 = Dog("Labrador Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

dog1.show_details()
dog2.show_details()
