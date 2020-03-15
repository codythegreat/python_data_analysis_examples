# printData.py - Showcases the ability to print data by simply
#                using the print statement and the string
#                interpolation features that come with python 3.6
#                Uses empData.json

import matplotlib.pyplot as plt
import json
import pprint
import re
import numpy as np

class Person:
  def __init__(self, fName, lName, lat, lon):
    self.firstName = fName
    self.lastName = lName
    self.latitude = lat
    self.longitude = lon


if __name__ == "__main__":
    # data will hold our json data
    data = json.load(open('empData.json'))

    # create instances of person
    people = []
    for person in data:
        fName = person.get("name").get("first")
        lName = person.get("name").get("last")
        lat = float(person.get("latitude"))
        lon = float(person.get("longitude"))
        people.append(Person(fName, lName, lat, lon))

    # using f strings we can easily print these to a readable format
    for p in people:
        print(f'{p.firstName} {p.lastName} is at latitude {p.latitude} and longitude {p.longitude}')
    print()

    # or we could print in a table style format
    print('Name'.ljust(20, ' ')+'Location')
    for p in people:
        print(f'{p.firstName} {p.lastName}'.ljust(20, ' ')+f'Lat: {p.latitude}'.ljust(16, ' ')+ f'Long: {p.longitude}')