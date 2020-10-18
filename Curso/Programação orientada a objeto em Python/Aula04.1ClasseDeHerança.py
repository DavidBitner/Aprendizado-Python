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


class MissingPerson(Person):
    def __init__(self, name, photo, date_of_birth, date_missing):
        Person.__init__(self, name, photo, date_of_birth)
        self.missing_since = date_missing

    def get_years_missing(self):
        return int((datetime.datetime.now() - self.missing_since).days / 365.25)


# Load the dataset
faces = fetch_olivetti_faces()

aPerson = MissingPerson("Adam", faces.images[0], datetime.datetime(1990, 9, 16), datetime.datetime(2016, 1, 1))
print(f"{aPerson.name} has been missing for {aPerson.get_years_missing()} years")
print(dir(aPerson))
