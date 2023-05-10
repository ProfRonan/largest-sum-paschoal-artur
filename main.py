"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if numbers:
        numbers.sort()
        popped_num = numbers.pop()
        popped_num2 = numbers.pop()
        print(f"({popped_num2}, {popped_num})")
    else:
        print("None")
    return popped_num, popped_num2