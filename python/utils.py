

def max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if max_num < num:
            max_num = num
    return max_num


