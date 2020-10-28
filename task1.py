#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
import tkinter as tk
import os

pets = []

class pet:

    global pets

    def __init__(self):
        self.animal = input("Type of animal:\n")
        self.breed = input("Breed:\n")
        self.name = input("Name:\n")
        self.owner = input("Owner:\n")
        self.birth = input("Birthdate\n")

    def __del__(self):
        pass

    def display(self):
        print( self.name + " " + self.animal + " " + self.breed + " " + " is owned by " + self.owner)

def main():
    global pets
    global pet
    y = True
    while y == True:
        x = input("Enter 1, 2, or 3\n1. Enter a new pet\n2. Retrieve a pet\n3. Exit\n")
        if x == "1":
            pets.append(pet())
            os.system("cls")
        elif x == "2":
            if len(pets) == 0:
                os.system("cls")
                print("You have no pets!")
            else:
                os.system("cls")
                p = input("Enter pet's name\n")
                if p in pets:
                    pets[pets.intex(p)].display()
                else:
                    os.system("cls")
                    print("You don't have a pet named " + p + "!")
        elif x == "3":
            os.system("cls")
            print("Yeah get outta here loser")
            break
        else:
            os.system("cls")

main()




"""
main = tk.Tk()
main.title("PETS")
main.mainloop()
"""