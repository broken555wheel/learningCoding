a = input()
set_a = set(map(int, a.split()))
n = int(input())
sets = []
for i in range(n):
    sets.append(set(map(int, input().split())))
superset = all(set_a > x for x in sets)
print(superset)
