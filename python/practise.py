try:
    age = int(input("Age: "))
    print(age)
except ValueError as e:
    print(f"Invalid value: {e}")