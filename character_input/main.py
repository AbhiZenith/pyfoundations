# Program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old.

from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# The years left when the user turns 100 years old
left_years = 100 - age

current_year = datetime.now().year

# The year when the user will turn 100 years old
year_of_100 = current_year + left_years

# Tells the user the year they will turn 100 years old
print(f"{name}, you will turn 100 years old in the year {year_of_100}")
