def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    fib_n_1 = fibonacci(n-1)
    fib_n_2 = fibonacci(n-2)
    output = fib_n_1 + fib_n_2
    return output

n = int(input("Enter number: "))

for i in range(1,n+1):
    result = fibonacci(i)
    print(result, end=" ")

