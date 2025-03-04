def sum_nth_numbers(n):
    if n == 0:
        return 0
    smallOutput = sum_nth_numbers(n-1)
    return n + smallOutput

result = sum_nth_numbers(5)
print(result)