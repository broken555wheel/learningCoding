# Maps/ ChainMap is used to manage multiple dictionaries as one unit, having key and value pairs in a certain
# sequence therefore eliminating duplicate keys.
# They behave like a stack data structure
# Chainmaps are the alternative to creating new dictionaries and running .updates() since they are faster
import collections
dict1 = {"day1": "Monday", "day2":"Tuesday"}
dict2 = {"day3": "Wednesday", "day4":"Thursday"}
cmap = collections.ChainMap(dict1, dict2)
print(cmap)