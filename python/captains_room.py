from collections import Counter

k = int(input())
room_numbers = input()
room_numbers = room_numbers.split()  # split method separates the string as per the characters defined within the
# string. The elements are converted into a list

list_rooms = list(map(int, room_numbers))  # map applies a function to each element of an iterable. In this case,
# int() is applied to each element of room_numbers

rooms_counts = Counter(list_rooms)  # Counter is used to count the number of times an element appears in an
# iterable. It creates a dict with keys(elements) and values(no. of appearances)
for num, count in rooms_counts.items():  # loop that iterates over the dictionary. num is the key, count is the
    # value. .items() obtains the key-value pairs as tuples. rooms_counts.items() returns an iterable view where each
    # element is a tuple representing a key-value pair.
    if count != k:
        print(num)
