# contiguous block of memory used to store data of the same data type
# operations:- Traversal, Insertion, Deletion, Search, Update
from array import *


numbers = array('i', [1, 2, 3, 4, 5, 6, 7])
# typcodes and their values
# b - i1 byte integer
# B - 1 byte unsigned integer
# c - 1 byte char
# i - 2 byte integer
# I - 2 byte unsigned integer
# f - 4 byte float
# d - * byte float

# traversal - outputting each element of the array
for num in numbers:
    print(num)
# access - outputting an element at a particular index
print(numbers[2])
# deletion - removing an element from te array
numbers1 = numbers.__copy__()
numbers1.remove(6)  # remove() - removes numbers by value wheres del() removes elements by index
for num in numbers1:
    print(num)
# insertion - adding an element to the array
numbers.insert(8, 10)  # if the index is greater than array length, the new element will be inserted at
# the end of the array
for num in numbers:
    print(num)
# updating - changing an element at a particular index
numbers[5] = 18
# searching - finding the index of an element
print(numbers.index(10))

# 2D ARRAYS (nested list)
# end = : used to specify the separation of multiple printed characters if we need not have the default newline char
my_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12, ]]
for i in my_array:
    for j in i:
        print(j, end=" ")  # ensures that the separator of multiple elements is a space not a newline
    print()  # adds a newline after each array is printed
# insertion
my_array.insert(3, [5, 6, 7, 8])
# updating
my_array[3] = [7, 8, 9, 10]
my_array[1][3] = 500
# deletion
del (my_array[2][2])

# Matrix - a 2d array where each element is strictly of the same size
from numpy import *  # allows us to create a matrix
weekly_temp = array(
    [['Monday', '35', '36', '38', '32'], ['Tuesday', '33', '37', '32', '28'], ['Wednesday', 33, '37', 32, '28'],
     ['Thursday', '33', '37', '32', '28'], ['Friday', '33', '37', '32', '28'], ['Saturday', '33', '37', '32', '28'],
     ['Sunday', '33', '37', '32', '28']])
temps = reshape(weekly_temp, (7, 5))  # reshape(array, (int tuple)) - defines the way our data
# structure is reshaped
print(temps)
# access and updating is similar to 2d arrays
# adding a row
temps2 = append(temps, [['Avg', 'x', 'y', 'z', 'a']], 0)  # 0 for crow, 1 for column
temps2 = delete(temps2, [1], 0)
print(temps2)
