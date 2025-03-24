def addition():
    return 2 + 2


def multiplication():
    return 3 * 9


def finding_max_no(numbers):
    max_no = numbers[0]
    for number in numbers:
        if number > max_no:
            max_no = number
    # print(f'The maximum number is {max_no}')
    return max_no

# numbers = [2, 1]
# max = finding_max_no(numbers)
# print(max)
# print(f'The maximum no is {finding_max_no()}')
