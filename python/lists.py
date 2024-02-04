# LISTS
# list()- function used to convert items into lists
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0])  # indexing is used to print individual elements(similar to strings)
# largest number
num = [12, 14, 18, 11, 16]
max_num = num[0]
for x in num:
    if max_num < x:
        max_num = x
print(max_num)

# 2D lists
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# Accessing of individual elements is done by indexing
# Looping is done using nested for loops
for a in matrix:
    for b in a:
        print(b)  # prints all the elements in the list

# LIST METHODS
numbers = [5, 2, 5, 2, 2]
numbers.append(20)  # adds the number at the end of the list
print(numbers)
numbers.extend([13, 12, 12, 13, 14])  # adds the list within extend to the end of the list
numbers.insert(0, 10)  # used to add an element at a specific index i.e. list.insert(index,element)
numbers.remove(11)  # used to remove an element from the list
numbers.clear()  # used to delete all the elements in the list
numbers.pop()  # removes the last element in our list (also in arrays)
numbers.index(12)  # returns the index of the element and if it doesn't exist, an error is returned
print(12 in numbers)  # returns a boolean expression depending on whether the element exists in the list
numbers.count(11)  # returns the number of times an element appears in a list
numbers.sort()  # doesn't return a value, instead sorts the list
numbers4 = sorted(numbers)  # returns a new sorted list without altering the original list
numbers.reverse()  # reversed the list
numbers2 = numbers.copy()  # copies the elements of list1 into list2
# REMOVING DUPLICATES
num2 = [4, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10]
# modifying a list while iterating over it can lead to unexpected behavior.
uniques = []
for z in num2:
    if z not in uniques:
        uniques.append(z)
print(uniques)

# List comprehension
# It is a concise and expressive way to create lists in Python. It provides a more readable and
# compact syntax for generating lists compared to using traditional loops. The basic syntax of a list
# comprehension is as follows:
# [expression for item in iterable if condition]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
my_list = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]  # list
# comprehension
print(my_list)

# ranking
students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
students = sorted(students, key=lambda x: x[1])
students_marks = list(set(sublist[1] for sublist in students))
second_lowest_score = sorted(students_marks)[1]
names = [name for name, score in students if score == second_lowest_score]
names.sort()
for name in names:
    print(name)
