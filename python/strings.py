course = 'Python\'s course for beginners'  # escape characters can be used to prevent termination of the string
course = "Python's course for beginners"
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
print(course.upper())  # method used to capitalize all characters in a string. .lower() changes them to lowercase.
# .title() makes the first character of each word capital. .swapcase() inverts the case of each character
print(course.find('P'))  # find() - case sensitive method that returns the index of a character or the beginning
# index of a word
print(course.replace("course", "class"))  # case-sensitive method used to replace a character or a sequence of
# characters. The character(s) to be replaced is placed first, then the replacer second.
print("Python" in course)  # in expression is used to check whether characters are in a string.
# It produces boolean values