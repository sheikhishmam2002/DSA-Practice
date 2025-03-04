def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
    return

print_1_to_n(10)