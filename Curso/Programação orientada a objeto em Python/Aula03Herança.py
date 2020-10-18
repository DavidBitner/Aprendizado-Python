from sklearn.datasets import fetch_olivetti_faces
import datetime


class Person:
    def __init__(self, name, photo, date_of_birth):
        self.name = name
        self.photo = photo
        self.dob = date_of_birth

    def get_age(self):
        return int((datetime.datetime.now() - self.dob).days / 365.25)

    def __str__(self):
        return f"{self.name}, age {str(self.get_age())}"


# Load the dataset
faces = fetch_olivetti_faces()

# Person
aPerson = Person("Adam", faces.images[0], datetime.datetime(1990, 9, 16))

# Prints
print(str(aPerson))
print(aPerson.__str__())
print(aPerson)
