# A group of non-repeated values
Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
Weekend = {"Saturday", "Sunday", "Funday"}
# adding an element
Names = {"David", "Mwalimu"}
Names.add("Nzambuli")
# deleting an element
Weekend.discard("Funday")
# Union of sets
AllDays = Days | Weekend
print(AllDays)
# intersection of sets - returns values shared by the sets
Intersection = Days & Weekend
print(f"Days^Weekend = {Intersection}")
# set difference
Difference = Days - Weekend
print(f"Days-Weekends = {Difference}")
# Set comparisons - return boolean values
print(AllDays >= Days)  # AllDays is a superset of days
print(Weekend <= Days)  # Weekend iis not a subset of Days

# checking strict supersets for n number of sets
a = input()
set_a = set(map(int, a.split()))
n = int(input())
sets = []
for i in range(n):
    sets.append(set(map(int, input().split())))
superset = all(set_a > x for x in sets)  # checks if all elements meet the specified criteria. Any checks if at least
# one does. Returns boolean values
print(superset)

# finding runners-up
n = int(input())
arr = map(int, input().split())
unique_scores = list(set(arr))
unique_scores.sort(reverse=True)
runner_up = unique_scores[1]
print(runner_up)
