# Linear_search

def linear_search(list, target):
    for n in list:
        if target == n:
            return f"{target} exists at position {list.index(n)}"
    return f"{target} does not exist within the list provided"
    

numbers = [12,13,10,54,34,14,436,45,45,76,43,73]
num_to_be_found = 54

print(linear_search(numbers, num_to_be_found))