import datetime

print("welcomme to the interactive personal data collector!\n")

current_datetime = datetime.datetime.now()

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height in meters:"))
fav_number=int(input("please enter your favorite number:\n"))

print("Thank you ! here is the information we collected:\n")


print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favorite Number: {fav_number} (Type: {type(fav_number)}, Memory Address: {id(fav_number)})")

birth_year=current_datetime.year-age

print("\n")

print(f"Your birth year is approximately {birth_year} (based on your age of {age})\n")


print("Thank you for using the personal data collector. Goodbye!")