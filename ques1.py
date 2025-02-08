print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

current_year = 2025 
birth_year = current_year - age

print("\nThank you! Here is the information we collected:\n")
print("Name: " + name + " (Type: " + str(type(name)) + ", Memory Address: " + str(id(name)) + ")")
print("Age: " + str(age) + " (Type: " + str(type(age)) + ", Memory Address: " + str(id(age)) + ")")
print("Height: " + str(height) + " (Type: " + str(type(height)) + ", Memory Address: " + str(id(height)) + ")")
print("Favourite Number: " + str(fav_number) + " (Type: " + str(type(fav_number)) + ", Memory Address: " + str(id(fav_number)) + ")")

print("\nYour birth year is approximately: " + str(birth_year) + " (based on your age of " + str(age) + ")")
print("\nThank you for using the Personal Data Collector. Goodbye!")
