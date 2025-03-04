def factorial (n):
    if n == 0: # Base case
        return 1
    smallOutput = factorial(n-1) # assumption
    return n*smallOutput

n = int(input("Enter number:\n"))
result = factorial(n)
print(result)