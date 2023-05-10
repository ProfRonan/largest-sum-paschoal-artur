"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if len(numbers) > 1 :
        numbers.sort()
        popped_num = numbers.pop()
        popped_num2 = numbers.pop()
        print(f"({popped_num2}, {popped_num})")
        return popped_num2, popped_num
    else:
        return None
