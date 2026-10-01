# Lesson 1: print() and variables
# Run this file:  python lessons/01_print_and_variables.py

# --- 1. print() shows things on the screen ---
print("Hello, Python!")
print("You can print", "several things", "at once")

# --- 2. Variables are names that point to values ---
name = "Akhil"          # str   (text)
age = 30                # int   (whole number)
height = 1.75           # float (decimal number)
is_learning = True      # bool  (True or False)

print(name, age, height, is_learning)

# type() tells you what kind of value something is
print(type(name), type(age), type(height), type(is_learning))

# --- 3. f-strings: put variables inside text ---
print(f"My name is {name} and next year I'll be {age + 1}.")

# --- 4. Basic math ---
print(7 + 3)    # 10   addition
print(7 - 3)    # 4    subtraction
print(7 * 3)    # 21   multiplication
print(7 / 3)    # 2.333... division (always gives a float)
print(7 // 3)   # 2    floor division (drops the decimal)
print(7 % 3)    # 1    remainder ("modulo")
print(7 ** 3)   # 343  power

# --- 5. Getting input from the user ---
# input() always returns text (str), so convert it with int() for numbers.
# Uncomment the next two lines to try it:
favorite = input("What's your favorite number? ")
print(f"Double your favorite number is {int(favorite) * 2}")



# ================== YOUR TURN ==================
# Write your answers below, run the file, and check the output.
#
# Exercise 1: Create a variable `city` with the city you live in,
#             and print "I live in <city>" using an f-string.
#
# Exercise 2: Store the price of an item (e.g. 250.0) and a quantity (e.g. 3).
#             Print the total cost.
#
# Exercise 3: Ask the user for their birth year with input(),
#             and print roughly how old they are in 2026.
