from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    s = sorted(s)
    for size in range(1, int(k) + 1):
        perms = permutations(s, size)
        for p in perms:
            print(''.join(p))
# prints permutations of string s, starting from a length of 1 to k+1
# combinations instead of permutations yields non-repeated strings in the above code
