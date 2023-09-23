print("David Mwalimu")
print("o----")
print(" ||||")
print("*"*10)
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
print(name1+" likes the color "+color)

# TYPE CONVERSION
birth_year = input("Birth year: ")  # whatever is typed in the terminal is i.e. from the input function is a string
age = 2023 - int(birth_year)
print(age)

# calculator
name2 = input("What is your name? ")
print("Hi " + name)
num1 = int(input("Enter the first number: "))  # type conversion from the get go
num2 = input("Enter the second number: ")
sum = num1+int(num2)
print(type(num1))  # type() is an inbuilt function used to display the value's datatype
print("The sum of ", num1 , " and " + num2 + " is ", sum)  # concatenation of a string and an int

# pounds to kg
pounds = int(input("Enter your weight in pounds: "))
kg = float(pounds)*0.453592
print("You weigh ", pounds, "pounds which is equivalent to ", kg, " kgs")


# STRINGS
course = "Python's course for beginners"
course = 'Python\'s course for beginners'  # escape characters can be used to prevent termination of the string
# tripple quotes can be used to write multi-line strings
print(course[0])  # indexing - used to get the value of a string at a particular index, starting from 0
# negative indexing i.e. course[-1] are used to access characters from the end of the string
print(course[0:3])  # returns multiple characters i.e the characters from the first number to the one before the last
# one
print(course[0:])  # prints all the characters in the string. The end of the string is assumed to be the end index
print(course[:5])  # prints all characters up to the fifth. 0 is assumed to be the starting index by the interpreter.
print(course[:])  # prints all the characters of the string
print(course[1:-1])  # prints all the characters up to the one before the last one(pretty simple)


# FORMATTED STRINGS
# variable names should be descriptive
first = "John"
last = "Smith"
message = first + '['+last+'] is a coder'
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
print("Python" in course)  # in expression is used to check whether characters are in a string. It produces boolean values


# ARITHMETIC OPERATIONS
# +: addition
# -: subtraction
# /: float division
# //: int division
# **: exponent
# x+(-,/,*)=3: augmented assignment operator
# exponentiation
# multiplication/division

# operation precedence
# parenthesis
# addition/subtraction


# MATH FUNCTIONS
x=2.9
print(round(x))  # rounds off a number
# abs() returns the absolute value of a number
# import math - used to import the math method.
# math.ceil(a) - rounds up a number
# python3 math module for others


#IF STATEMENTS
is_hot = True;
if is_hot:
    print("It's a hot day, enjoy your day")
    print("Drink plenty of water") # indented statements will be executed if the evaluation is true
# elif can be used if there are more conditions
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

# buying a house
price = 1000000
good_credit = input("Is the credit score good?(y or n)")
if good_credit.upper() == "Y":
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(down_payment)


#LOGICAL OPERATORS
# logical and returns true if both conditions evaluate to true
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
# logical or returns true if either of the statements is true
# logical not returns the opposite boolean value
if has_high_income or not has_good_credit:
    print("Not eligible for loan")


# COMPARISON OPERATORS
# a>b a greater than b
# a==b a is equivalent to b
# a<b a is less than b
# a!=b a is not equal to b

# Client name
client_name = input("What is your name? ")
if len(client_name)<3:
    print("Error! Name is too short")
elif len(client_name)>50:
    print("Error! Name is too long")
else:
    print("Name looks good")

# weight converter
weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight_new = weight*0.453592
    print(weight_new)
elif unit.upper() == "K":
    weight_new = weight/0.453592
    print(weight_new)
else:
    print('Invalid unit entered. Enter a unit that is either L for pounds or K for kilograms')


# WHILE LOOPS
# used to execute a block of code as long as a condition remains true
i = 1
while i <= 5:
    print("*" * i)
    i += 1

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
# we can have a while else statement where the else portion is executed when the condition in the while loop evaluates
# to false


# FOR LOOPS