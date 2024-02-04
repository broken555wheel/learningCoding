import random
import module  # used to import modules
from module import pounds_to_kg  # used to import a specific module method
from pathlib import Path
# In interactive mode, the last printed expression is assigned to the variable _.
# Python hs support for complex numbers and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j)
# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by
# adding an r before the first quote. A raw string may not end in an odd number of '\'

print("David Mwalimu")
print("o----")
print(" ||||")
print("*" * 10)  # prints * 10 times
# the above code is an expression i.e. it produces a value


# VARIABLES
# they are used to temporarily store data in memory
price = 10  # integer
rating = 4.9  # floating point
name = "David"  # string
is_published = False  # boolean(Must start with a capital letter due to case sensitivity)
price = 20  # changes the value to 20 as python executes code line by line
print(price)

# patient John
patient_name = "John Smith"
patient_age = 20
patient_new = True

# GETTING INPUT
# input()-inbuilt function used to get user input
name = input("What is your name? ")
print("Hi " + name)  # string concatenation
# the variable name assigned to input is where the user input will be stored

# two questions
name1 = input("What is your name? ")
color = input("What is your favorite color? ")
print(name1 + " likes the color " + color)

# TYPE CONVERSION
birth_year = input("Birth year: ")  # whatever is typed in the terminal is i.e. from the input function is a string
age = 2023 - int(birth_year)
print(age)

# calculator
name2 = input("What is your name? ")
print("Hi " + name)
num1 = int(input("Enter the first number: "))  # type conversion from the get go
num2 = input("Enter the second number: ")
sum3 = num1 + int(num2)
print(type(num1))  # type() is an inbuilt function used to display the value's datatype
print("The sum of ", num1, " and " + num2 + " is ", sum3)  # concatenation of a string and an int

# pounds to kg
pounds = int(input("Enter your weight in pounds: "))
kg = float(pounds) * 0.453592
print("You weigh ", pounds, "pounds which is equivalent to ", kg, " kgs")

# STRINGS
course = "Python's course for beginners"
course = 'Python\'s course for beginners'  # escape characters can be used to prevent termination of the string
# triple quotes can be used to write multi-line strings
print(course[0])  # indexing - used to get the value of a string at a particular index, starting from 0
# negative indexing i.e. course[-1] are used to access characters from the end of the string
print(course[0:3])  # returns multiple characters i.e. the characters from the first number to the one before the last
# one
print(course[0:])  # prints all the characters in the string. The end of the string is assumed to be the end index
print(course[:5])  # prints all characters up to the fifth. 0 is assumed to be the starting index by the interpreter.
print(course[:])  # prints all the characters of the string
print(course[1:-1])  # prints all the characters up to the one before the last one(pretty simple)
# out of range slice indexes are handled gracefully when used for slicing
print(course[0:50])  # no error will be returned
# FORMATTED STRINGS
# variable names should be descriptive
first = "John"
last = "Smith"
message = first + '[' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'  # f'' refers to a formatted string
# Curly braces({}) are used as placeholders for our variables and allow us to dynamically insert values into our strings
# message == msg


# STRING METHODS
print(len(course))  # len() - string method used to find the length of a value
# dot operator is used to access object(string) methods
print(course.upper())  # method used to capitalize all characters in a string. .lower() changes them to lowercase
print(course.find('P'))  # find() - case sensitive method that returns the index of a character or the beginning
# index of a word
print(course.replace("course", "class"))  # case-sensitive method used to replace a character or a sequence of
# characters. The character(s) to be replaced is placed first, then the replacer second.
print("Python" in course)  # in expression is used to check whether characters are in a string.
# It produces boolean values

# ARITHMETIC OPERATIONS
# +: addition
# -: subtraction
# /: float division
# //: int division
# **: exponent
# x(+,-,/,*)=3: augmented assignment operator
# operation precedence
# exponentiation
# parenthesis
# multiplication/division
# addition/subtraction
# mixed operations convert integers to floats

# MATH FUNCTIONS
x = 2.9
print(round(x))  # rounds off a number
# abs() returns the absolute value of a number
# import math - used to import the math method.
# math.ceil(a) - rounds up a number. math.floor() - rounds down a number
# python3 math module for others


# IF STATEMENTS
# created by indenting statements after the conditional block
is_hot = True
if is_hot:
    print("It's a hot day, enjoy your day")
    print("Drink plenty of water")
# indented statements will be executed if the evaluation is true
# elif can be used if there are more conditions
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

# buying a house
price = 1000000
good_credit = input("Is the credit score good?(y or n)")
if good_credit.upper() == "Y":
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(down_payment)

# LOGICAL OPERATORS
# logical and returns true if both conditions evaluate to true
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
# logical or returns true if either of the statements is true
# logical not returns the opposite boolean value
if not has_high_income or not has_good_credit:
    print("Not eligible for loan")

# COMPARISON OPERATORS
# a>b a greater than b
# a==b a is equivalent to b
# a<b a is less than b
# a!=b a is not equal to b

# Client name
client_name = input("What is your name? ")
if len(client_name) < 3:
    print("Error! Name is too short")
elif len(client_name) > 50:
    print("Error! Name is too long")
else:
    print("Name looks good")

# weight converter
weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight_new = weight * 0.453592
    print(weight_new)
elif unit.upper() == "K":
    weight_new = weight / 0.453592
    print(weight_new)
else:
    print('Invalid unit entered. Enter a unit that is either L for pounds or K for kilograms')

# WHILE ELSE LOOPS
# used to execute a block of code as long as a condition remains true
i = 1
while i <= 5:
    print("*" * i)
    i += 1  # incrementer used to ensure that the loop does not run infinitely in this case

# guessing game
correct = 12
tries = 0
guess_limit = 5
while tries < guess_limit:
    guess = int(input("Guess a number: "))
    tries += 1
    if guess == correct:
        print(f"{guess} is the correct guess")
        break  # terminates our loop
else:
    print("Sorry, you failed")
# we can have a while-else statement where the else portion is executed when the condition in the while loop evaluates
# to false


# FOR LOOPS
for item in "Python":  # item is set to each letter for each iteration
    print(item)
# lists in python are defined using []
for item in ["David", "Mwalimu", "Nzambuli"]:
    print(item)
# range() - inbuilt function used to set the range(an object) for a given set of numbers
for item in range(10):  # Includes 0,1,2,3,4,5,6,7,8,9
    print(item)
# range(x,y) - includes numbers from x to y-1
# range(x,y,2) -includes numbers from x to y-1, with a common difference of 2

# Total Cost of items
prices = [10, 20, 30]
sum1 = 0
for item in prices:
    sum1 += item
print(sum1)

# NESTED LOOPS
for x in range(4):  # sample x coordinate
    for y in range(3):  # sample y coordinate
        print(f"{x},{y}")
# for each outer iteration, all inner iterations must be executed

# F SHAPE
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("*" * number)  # Multiplying a string by a number prints the string as many times as the number it is
# being multiplied with
# using nested loop
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# TUPLES
# Similar to lists but are immutable
numbers3 = (1, 2, 3)  # defining a tuple
# a tuple has count and index as its method with the rest being magic methods
# when declaring a tuple with a single element, use a comma at the end i.e
my_tuple = ("David",)
tuple3 = numbers3 + my_tuple  # adding of elements in different tuples to yield a new tuple
# Tuple operations: iteration, concatenation, membership, length, repetition

# UNPACKING
coordinates = (1, 2, 3)
a1, a2, a3 = coordinates  # assigns the elements in the tuple to the variables on the left respectively


# unpacking can also work for lists
# a list can also be unpacked into function arguments as follows
def func(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]
func(*my_list)  # list elements become the arguments in the function


# the number of arguments must be the same as the length of the list we are unpacking

# we can use packing to pass arguments into a tuple if we do not know the number of arguments
def func2(*args2):
    return sum(args2)


print(func2(11, 30, 35))  # the sum of any number of values passed as arguments will be printed

# DICTIONARIES used to store values that comes as key value pairs
# values in a dictionary can be of any data type (including lists and tuples)and
# can be duplicated, whereas keys can’t be repeated and must be immutable
# dict({key:value}) - method used to create a dictionary
# only one entry is allpwed per key
client = {
    "Name": "John Smith",
    "Age": 30,
    "is_verified": True
    # each key should be unique
}
# access is done using [] i.e.
print(client["Name"])  # case-sensitive and must have the quotes
# if the key doesn't exist, an error will be thrown alternatively, we could use the get method which does not throw
# an error in case the key doesn't exist. It instead returns none dictionary.get(key, default)
print(client.get("name"))  # returns None since it's also case-sensitive
# we can also use get to define a new key value pair
print(client.get("Birthday", "March 11th 2004"))  # only prints the value pair, does not mutate the dictionary
# we can also update and add values using []
client["Height"] = "6'2"  # adding a new key value pair
client["Name"] = "David Mwalimu"  # changing an existing key value pair
# we can also use the dictionary.update() method to update/ add onto a dictionary dictionary.update({key:value})
client.update({"Name": "David Nzambuli", "Employment": "Data Analyst"})  # overwrites the Name key and adds employment
# we can delete key value pairs using the del() method i.e. del(dictionary[key])
del (client["Age"])  # deletes the Age key value pair
# dictionary.keys() - returns dict_keys(list of all the keys in the dictionary)
print(client.keys())
# dictionary.values() - returns dict_values(list of all values in the dictionary)
# NUMBERS TO WORDS
phone = input("Phone: ")
digits = {
    "1": "one",
    "0": "zero",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for x in phone:
    output += digits.get(x, "!") + " "
print(output)
# EMOJI CONVERTER
message = input(">")
words = message.split(" ")  # .split() is a methods used to separate  string with the separation happening at the point
# defined in the split method. It returns a list with the separation making the elements. The split element is not
# returned
emojis = {
    ":)": "😁",
    ":(": "😌"
}
output2 = ""
for word in words:
    output2 += emojis.get(word, word) + ""
print(output2)


# FUNCTIONS
# def is a  keyword used to define functions
def greet_user():
    print("Hi There!")
    print("Welcome aboard!")


print("Start")
greet_user()
print("Finish")


# a function must always be called after it is defined

# PARAMETERS
# values taken by a function
def greet_user2(name):
    print(f"Hi {name}")
    print("Welcome Aboard")


name3 = input("What is your name? ")
greet_user2(name3)


# if a parameter is set for a function, the argument must be provided otherwise an error will be returned
# for positional arguments, the position matters i.e. they will be returned in the order they are provided

# KEYWORD ARGUMENTS
# defined using the parameter name when providing the arguments
def greet_user3(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet_user3("Nzambuli", first_name="David")  # keyword argument


# Keyword arguments should always come after positional arguments

# RETURN STATEMENT
# used to produce the output of a function
def square(number):
    return number ** 2


print(square(16))
# without the return statement, the function will return None(represents the absence of a value) when we print the
# output of the function if we replace the return with print, we get both the square and None as output

# CREATING A REUSABLE FUNCTION
text = input(">")


def emoji_converter(user_input):
    words1 = user_input.split(" ")
    emojis1 = {
        ":)": "😄",
        ":(": "😟",
        ":|": "😐"
    }
    output3 = ""
    for word1 in words:
        output3 += emojis.get(word1, word1) + " "
    return output3


print(emoji_converter(text))
# input and output shouldn't be included in functions since they should be reusable

# EXCEPTIONS
# exit code 0 means that our program executed with no problem
# raise keyword is used to return an error
u = -1
if u < 0:
    raise ValueError("x should be a positive number")
# anything but 0 means that our program crashed
# NameError - Raised when a local or global name is not found
# KeyError - Raised when a dictionary key is not found.
# AttributeError - Raised when an attribute reference or assignment fails.
# FileNotFoundError - Raised when a file or directory is requested but cannot be found.
# TypeError - Raised when an operation or function is applied to an object of an inappropriate.
# ValueError - Raised when a function receives an argument of the correct type but with an invalid value.
# ZeroDivisionError - Raised when division or modulo by zero is encountered.
# try except is used to handle errors
try:
    miaka = int(input("Age: "))
    print(age)
except ValueError as e:
    print(f"Invalid value: {e}")


# at the except you type of error that could occur
# there can be many except used to anticipate different errors
# we can use an else block to execute code if the try doesn't fail
# a finally block can also be added. It will be executed regardless

# COMMENTS - used to explain why and how not what r.g assumptions

# CLASSES
# used to model real world objects
# pascal naming convention(used for classes where you capitalize the first letter)
class Point:
    def __init__(self, x, y):
        self.x = x  # same as saying point = Point() \n point.x = 10
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# creating an object
# var_name = ClassName()
# point1 = Point()
# assigning attributes to objects
# point1.x = 10

# CONSTRUCTORS
# It is a function that gets called when defining an object
# __init__(self, parameter1,..., parameterN):
# self.x = x \n self.y = y
# we can change the attribute of an object by object_name.attribute_name = new_value
# person class
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


# INHERITANCE
# where a clas inherits a method from its parent class
# python doesn't like an empty class, and to sort this out you can use pas
# class ClassName(ParentClassName):
class Mammals:
    def walk(self):
        print("walk")


class Dog(Mammals):  # inheritance where dog inherits from mammals
    def bark(self):
        print("bark")


# MODULES
# These are files with different python codes
# It enhances re-usability
# to import specific modules, use from filename import module
# when a module is imported it becomes an object so a dot operator is used to access its methods
print(module.kg_to_pounds(69))  # module importation
print(pounds_to_kg(153))  # specific module importation allows for direct use of functions


# PACKAGES
# a package is a container for related modules in pycharm, create a package file, and in the file create a
# file with the name __init__.py. This will be interpreted as a package
# Importing a module
# You can import the entire module i.e. import package_name.file_name
# To use functions in the module: module_name.method
# alternatively: from package_name.module_name import method1, ... , methodN

# IN BUILT MODULES
# from browser, lookup python 3 module index
# import module_name
# random.random() - generates  random number between 0 and 1
# random.randint(x,y) - generates a random integer between x and y
# random.choice(list_name) - returns a random element from a list
# Dice class
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # returns both values


dice = Dice()
print(dice.roll())

# FILES AND DIRECTORIES
# Absolute path - start rom the root directory and go elsewhere
# Relative path - start from the current directory and moves from there
# if we don't pass an argument in Path() it will reference the current directory
path = Path("ecommerce")
# .exist() method checks whether a path exists
print(path.exists())
# .mkdir() method is used to create new directories
path2 = Path("emails")  # makes a directory called emails
# .rmdir() - method that removes the directory assigned to the variable name where it is called
print(path.glob("*"))  # prints all the files and directories
print(path.glob("*.*"))  # prints only the files in the directory
print(path.glob("*.py"))  # print all the python files available in the directory
# we can use the above to iterate over the files available in the directory

# PIP AND PYPI
# python package index(PYPI) (pypi.org)
# to install a package from pypi, click it and run the command in the terminal
# after installing, you can import the package as a module
