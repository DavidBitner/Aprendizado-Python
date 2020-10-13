from sklearn.datasets import fetch_olivetti_faces
import datetime


class Person:
    def __init__(self, name, photo, date_of_birth):
        self.name = name
        self.photo = photo
        self.dob = date_of_birth


# Load the dataset
faces = fetch_olivetti_faces()

# Person
aPerson = Person("Adam", faces.images[0], datetime.datetime(1990, 9, 16))
print(aPerson.name)
